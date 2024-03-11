from rest_framework.decorators import api_view, APIView, permission_classes
from django.db.models import Q
from rest_framework.response import Response 
from rest_framework import status
from .auth_otp import generate_otp, send_otp_login_email, send_otp_phone
from .models import CustomUser, Address
from .serializer import UserSerializer, UserPatchCreateSerializer, UserPatchSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.utils import timezone

## Login system


class SendEmailOTP(APIView):
    def post(self, request):

        email = request.data.get('email', '')

        try:
            user = CustomUser.objects.get(email=email, is_active=True)

        except CustomUser.DoesNotExist:
            return Response({'error_email_does_not_exist': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        

        otp = generate_otp()
        user.otp = otp
        user.otp_expiration = timezone.now() + timezone.timedelta(minutes=3)
        user.save()

        send_otp_login_email(email, otp, user.first_name)

        return Response({'message': 'OTP has been sent to your email.', "success":True}, status=status.HTTP_200_OK)


class SendPhoneOTP(APIView):
    def post(self, request):

        phone = request.data.get('phone', '')

        try:
            user = CustomUser.objects.get(phone=phone, is_active=True)

        except CustomUser.DoesNotExist:
            return Response({'error_no_phone_account': 'User with this phone number does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        

        otp = generate_otp()
        user.otp = otp
        user.otp_expiration = timezone.now() + timezone.timedelta(minutes=3)
        user.save()

        send_otp_phone(phone, otp, user.first_name)

        return Response({'message': 'OTP has been sent to your phone number.', 'success':True}, status=status.HTTP_200_OK)
    




class ValidateOTPlogin(APIView):
    def post(self, request):

        email = request.data.get('email', '')
        phone = request.data.get('phone', '')
        otp = request.data.get('otp', '')
    

        try:
            user = CustomUser.objects.get(Q(Q(email=email) | Q(phone=phone)) & Q(otp=otp) & Q(is_active=True))
            
        except CustomUser.DoesNotExist:

            return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)


        
        if user.expired_otp:
            return Response({'error_login_expired_otp': 'OTP expired.'}, status=status.HTTP_400_BAD_REQUEST)
        

        if user.otp == otp:
            user.otp_expiration = None
            user.otp = None  
            user.save()

            serializer_user = UserSerializer(instance=user, many=False)

            return Response(serializer_user.data, status=status.HTTP_200_OK)
        
        else:
            return Response({'error_login_invalid_otp': 'Invalid OTP.'}, status=status.HTTP_400_BAD_REQUEST)




class LoginUserPhoneOTP(APIView):
    def post(self, request):

        email = request.data.get('email', '')
        phone = request.data.get('phone', '')

        try:
            user = CustomUser.objects.get(Q(Q(email=email) & Q(phone=phone)) & Q(is_active=True))
            
        except CustomUser.DoesNotExist:

            return Response({'error_mail': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)



        # Authenticate the user and create or get an authentication token
        token, _ = Token.objects.get_or_create(user=user)

        user_data = {
            'token': token.key
        }

        return Response(user_data, status=status.HTTP_200_OK)


class LoginUserEmailOTP(APIView):
    def post(self, request):

        email = request.data.get('email', '')
        phone = request.data.get('phone', '')
        otp = request.data.get('otp', '')

        try:
            user = CustomUser.objects.get(Q(Q(email=email) & Q(phone=phone)) & Q(is_active=True))
            
        except CustomUser.DoesNotExist:

            return Response({'error_mail': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)


        if user.expired_otp:
            return Response({'error_login_expired_otp': 'OTP expired.'}, status=status.HTTP_400_BAD_REQUEST)
        

        if user.otp == otp:
            user.otp_expiration = None
            user.otp = None  
            user.save()

            # Authenticate the user and create or get an authentication token
            token, _ = Token.objects.get_or_create(user=user)

            user_data = {
                'token': token.key
            }

            return Response(user_data, status=status.HTTP_200_OK)
        
        else:
            return Response({'error_login_invalid_otp': 'Invalid OTP.'}, status=status.HTTP_400_BAD_REQUEST)




## Login system


## User data


@api_view(['GET'])    
@permission_classes([IsAuthenticated])
def me(request):

    user_get = CustomUser.objects.get(Q(email=request.user.email) & Q(is_active=True))
    serializer_user = UserSerializer(instance=user_get, many=False)

    return Response(serializer_user.data, status=status.HTTP_200_OK)


## User data


## Register user system


@api_view(['POST'])
def register_user_email(request):
 
    email = request.data.get('email', '')


    if CustomUser.objects.filter(email=email).exists():
        return Response({'error_email_exists': 'User with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)
    

    otp = generate_otp()

    new_user = UserSerializer(data=request.data)
    new_user.is_valid(raise_exception = True)
    new_user.save()

    user = get_object_or_404(CustomUser, email=email)
    user.otp = otp
    user.is_active = False
    user.save()


    send_otp_login_email(email, otp, email)

    return Response({'message': 'OTP has been sent to your email.', "success":True}, status=status.HTTP_200_OK)


class ValidateOTPemail(APIView):
    def post(self, request):

        email = request.data.get('email', '')
        otp = request.data.get('otp', '')
    

        try:
            user = CustomUser.objects.get(Q(email=email) & Q(otp=otp) & Q(is_active = False))
            
        except CustomUser.DoesNotExist:
            return Response({'error_does_not_exist': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        

        if user.otp == otp:
            user.otp = None  
            user.email_confirmed_in = timezone.now()

            user.save()


            return Response({'message': 'Email OTP confirmed.', "success":True}, status=status.HTTP_200_OK)
        else:
            return Response({'error_invalid_otp': 'Invalid OTP.'}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PATCH'])
def register_user_phone(request):
 
    phone = request.data.get('phone', '')
    email = request.data.get('email', '')

    if CustomUser.objects.filter(phone=phone).exists():
        return Response({'error_phone_exists': 'User with this phone number already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    user = get_object_or_404(CustomUser, email = email)

    otp = generate_otp()
    user.otp = otp
    user.phone = phone
    user.save()

    send_otp_phone(phone, otp, email)

    return Response({'message': 'OTP has been sent to your phone number.', "success":True}, status=status.HTTP_200_OK)



class ValidateOTPphone(APIView):
    def post(self, request):

        phone = request.data.get('phone', '')
        otp = request.data.get('otp', '')
    

        try:
            user = CustomUser.objects.get(Q(phone=phone) & Q(otp=otp) & Q(is_active = False))
            
        except CustomUser.DoesNotExist:
            return Response({'error_does_not_exist': 'User with this phone number does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        

        if user.otp == otp:
            user.otp = None  # Reset the OTP field after successful validation
            user.phone_confirmed_in = timezone.now()
            user.save()


            return Response({'message': 'Phone OTP confirmed.', "success":True}, status=status.HTTP_200_OK)
        else:
            return Response({'error_invalid_otp': 'Invalid OTP.'}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PATCH'])
def register_user(request):

    user = get_object_or_404(CustomUser, email = request.data.get('email', ''))

    serializer = UserPatchCreateSerializer(instance=user,
                                            data=request.data, 
                                            many=False,
                                            partial=True,)
    serializer.is_valid(raise_exception=True)
 
    serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def edit_personal_data(request):
    
    user = get_object_or_404(CustomUser, id = request.data.get('id', ''))

    serializer = UserPatchSerializer(instance=user,
                                            data=request.data, 
                                            many=False,
                                            partial=True,)
    serializer.is_valid(raise_exception=True)
 
    serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)



## google

class GoogleLogin(SocialLoginView):

# https://dj-rest-auth.readthedocs.io/en/latest/installation.html#social-authentication-optional
    class GoogleAdapter(GoogleOAuth2Adapter):
        
        access_token_url = "https://oauth2.googleapis.com/token"
        authorize_url = "https://accounts.google.com/o/oauth2/v2/auth"
        profile_url = "https://www.googleapis.com/oauth2/v2/userinfo"

    adapter_class = GoogleAdapter
    # Callback URL was used by mobile app
    callback_url = "http://localhost:8000/"
    client_class = OAuth2Client



## google
    