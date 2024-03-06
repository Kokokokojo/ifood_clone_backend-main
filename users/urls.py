from django.urls import path
from .views import (LoginWithEmailOTP,
                    LoginWithPhoneOTP, 
                    ValidateOTP, me, register_user,
                      ValidateOTPemail, 
                      ValidateOTPphone, register_user_email, register_user_phone,
                      GoogleLogin, edit_personal_data
                      )


urlpatterns = [
    # Login Google
    path('authenticate/google/', GoogleLogin.as_view(), name='google_login'),
    # Login Google

    # Login email/telefone
    path('login-email-otp/', LoginWithEmailOTP.as_view(), name='login-with-otp-email'),
    path('login-phone-otp/', LoginWithPhoneOTP.as_view(), name='login-with-otp-phone'),
    path('validate-otp/', ValidateOTP.as_view(), name='validate-otp'),
    # Login email/telefone

    # Retornar dados do usuario
    path('@me/', me, name='me'),
    # Retornar dados do usuario

    # Registrar usuario email/telefone
    path('register-email/', register_user_email, name='register-email'),
    path('register-phone/', register_user_phone, name='register-phone'),
    path('validate-otp-email-register/', ValidateOTPemail.as_view(), name='validate-otp-email'),
    path('validate-otp-phone-register/', ValidateOTPphone.as_view(), name='validate-otp-phone'),
    path('register-user/', register_user, name='register-user'),
    # Registrar usuario email/telefone


    # Editar usuario 
    path('edit-user-personal-data/', edit_personal_data, name='edit-user-personal-data'),
    # Editar usuario 

]