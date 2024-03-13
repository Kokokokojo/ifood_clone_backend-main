from django.urls import path
from .views import (SendEmailOTP,
                    SendPhoneOTP, 
                    ValidateOTPlogin, me, register_user,
                      ValidateOTPemail, 
                      ValidateOTPphone, register_user_email, register_user_phone,
                      GoogleLogin, edit_personal_data, LoginUserPhoneOTP, LoginUserEmailOTP,
                      RegisterPhoneGoogle, ValidateGoogleOTPphone, edit_email, edit_email_confirm,
                      edit_phone, edit_phone_confirm
                      )


urlpatterns = [
    #  Google
    path('authenticate/google/', GoogleLogin.as_view(), name='google_login'),
    path('authenticate/google/google-register-phone/', RegisterPhoneGoogle.as_view(), name='google_login'),
    path('authenticate/google/google-validate-otp-phone/', ValidateGoogleOTPphone.as_view(), name='google_login'),
    #  Google

    # Login email/telefone
    path('login-email-otp/', SendEmailOTP.as_view(), name='login-with-otp-email'),
    path('login-phone-otp/', SendPhoneOTP.as_view(), name='login-with-otp-phone'),
    path('validate-otp/', ValidateOTPlogin.as_view(), name='validate-otp'),
    path('login-user-phone/', LoginUserPhoneOTP.as_view(), name='login-user-phone'),
    path('login-user-email/', LoginUserEmailOTP.as_view(), name='login-user-email'),
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
    path('edit-user-email/', edit_email, name='edit-email'),
    path('edit-user-email-confirm/', edit_email_confirm, name='edit-email-confirm'),
    path('edit-user-phone/', edit_phone, name='edit-phone'),
    path('edit-user-phone-confirm/', edit_phone_confirm, name='edit-phone-confirm'),
    # Editar usuario 

]