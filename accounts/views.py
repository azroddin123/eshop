from .serializers import *
from .models import *
from rest_framework.views import APIView
from portals.GM2 import GenericMethodsMixin
from rest_framework.response import Response
from rest_framework import status
from portals.services import generate_token
from django.contrib.auth.hashers import check_password
from random import randint
from portals.email_utility import send_email_async
from django.core.exceptions import ObjectDoesNotExist
from django.core.cache import cache


class UserApi(GenericMethodsMixin,APIView):
    model = User
    serializer_class = UserSerializer1
    lookup_field = "id"

class UserProfileAPI(APIView):
    def get(self,request,*args,**kwargs):
        # try :
            user_data = User.objects.get(id=request.thisUser.id)
            if user_data : 
                serializer = UserSerializer2(user_data)
            return Response({"error" : False, "data" : serializer.data},status=status.HTTP_200_OK)
        # except Exception as e :
        #     return Response({"error" : True , "message" : str(e)},status=status.HTTP_400_BAD_REQUEST)

from django.db import transaction
from portals.email_utility import send_email_async


API_KEY = "bcbc6fc9-14d9-11ef-8b60-0200cd936042"


class RegisterUserApi(APIView):
    def post(self,request,*args, **kwargs):
        try : 
            with transaction.atomic():
                print(request.data)
                email = request.data.get('email')
                mobile_number = request.data.get('mobile_number')                
                serializer = UserSerializer(data=request.data)
                email_otp = randint(100000,999999)
                sms_otp   = randint(100000,999999)
                request.POST._mutable = True
                request.data['email_otp'] = email_otp
                request.data['sms_otp']  = sms_otp 
                if  serializer.is_valid():
                    user = serializer.save()
                    token = generate_token(user.email)
                    message = "Your OTP for Email Verification "+str(email_otp)+"."
                    context = {"otp" : email_otp ,"username" : user.username }
                    subject = "Pride Motors OTP verification Email"
                    template_name = 'otp_email.html'
                    send_email_async(subject,template_name, context, [user.email])
                    return Response({"message" : "User Created Successfully" , "data" : UserSerializer1(user).data , "token" : token},status=status.HTTP_201_CREATED)
                error_list = [serializer.errors[error][0] for error in serializer.errors]
                return Response({"error": True, "message": error_list}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e :
            return Response({"error" : True , "message" : str(e) , "status_code" : 400},status=status.HTTP_400_BAD_REQUEST,)

class VerifyOTPApi(APIView):
    def post(self, request, *args, **kwargs):
        try : 
            email = request.data.get('email')
            email_otp = request.data.get('email_otp')
            # sms_otp = request.data.get('sms_otp')
            if not email or not email_otp :
                return Response({"error": True, "message": "Email, email OTP, and SMS OTP are required."}, status=status.HTTP_400_BAD_REQUEST)
            try:
                user = User.objects.get(email=email)
            except ObjectDoesNotExist:
                return Response({"error": True, "message": "User not found."}, status=status.HTTP_404_NOT_FOUND)
            if user.email_otp == email_otp:
                user.is_verified = True
                user.is_active = True
                user.status = True
                user.save()
                token = generate_token(user.email)
                return Response({"error": False, "message": "OTP verified successfully.","token" : token , "is_admin" : user.is_admin }, status=status.HTTP_200_OK)
            return Response({"error": True, "message": "Invalid OTP for email or SMS."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e :
            return Response({"error" : True , "message" : str(e) ,"status_code" : 400},status=status.HTTP_400_BAD_REQUEST,)

class ResendOTPApi(APIView):
    def post(self, request, *args, **kwargs):
        try:
                email     = request.data.get('email')
                user      = User.objects.get(email=email)
                email_otp = randint(100001,999999)
                user.email_otp = email_otp
                user.save()
                context = {"otp" : email_otp ,"username" : user.username }
                subject = "Vecto OTP verification Email"
                template_name = 'otp_email.html'
                send_email_async(subject,template_name, context, [user.email])
                return Response({"error": False, "message": "OTP Sent successfully."}, status=status.HTTP_200_OK)
        except Exception as e :
            return Response({"error" : True , "message" : str(e) , "status_code" : 400},status=status.HTTP_400_BAD_REQUEST,)

class LoginAPI(APIView):
    def post(self,request,*args, **kwargs):
        try : 
            email       = request.data.get('email')
            password    = request.data.get('password')
            user        = User.objects.filter(email=email).first()
            if user is None : 
             return Response({"error" : False,"message" : "User Not Exists"},status=status.HTTP_400_BAD_REQUEST)
            if user.is_verified  == False : 
                return Response({"error" : False,"message" : "Please Verify Your Email"},status=status.HTTP_400_BAD_REQUEST)
            token = generate_token(user.email)
            password_match = check_password(password,user.password)
            serializer = UserSerializer2(user)
            data = {"error" : False, "message": "User logged in successfully","user_info": serializer.data,"token" : token}
            if password == user.password  or password_match:
                return Response(data,status=status.HTTP_200_OK)
            return Response({"error" : True, "message" : "Password is not Matched"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e :
            return Response({"error" : True, "message" : str(e)},status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordApi(APIView):
    def post(self,request,*args, **kwargs):
        try : 
            serializer = ChangePasswordSerializer(data=request.data,context={'request': self.request})
            if serializer.is_valid():
                serializer.save()
                return Response({"Success": "Password updated successfully"},status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e :
                return Response({"error" : True, "message" : str(e)},status=status.HTTP_400_BAD_REQUEST)

class ForgotPasswordAPI(APIView):
    def post(self,request,*args, **kwargs):
        try :
            mail = request.data.get('email')
            print("in user",mail)
            user = User.objects.get(email=mail)
            print(user)
            email_otp = randint(100001,999999)
            user.email_otp = email_otp
            user.save()
            context = {"otp" : email_otp ,"username" : user.username , "message" : "We received a request to reset your password for your Vectosense account. No worries, we're here to help!" }
            subject = "Vecto Forget password OTP"
            template_name = 'otp_email.html'
            res = send_email_async(subject,template_name, context, [user.email])
            if (res ==1):
                return Response(data={'Success':'Otp Mail sent successfully'},status=status.HTTP_200_OK)
            else:
                return Response(data={"error": True,"message" : "Error sending Mail"},status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(data={"error": True,"message" : "User Email Does not exists"},status=status.HTTP_400_BAD_REQUEST )

class UpdateUserAPI(APIView):
    def put(self,request,*args, **kwargs):
        try :
            user = User.objects.get(id=request.thisUser)
            serializer = UserSerializer1(user, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"error" : False, "message": "User updated successfully",},status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e :
            return Response({"error" : True , "message" : str(e)},status=status.HTTP_400_BAD_REQUEST)
    
class ResetPasswordAPI(APIView):
    def post(self,request,*args, **kwargs):
        try : 
            email = request.data.get('email')
            password = request.data.get('password')
            if User.objects.filter(email=email):
                user = User.objects.get(email=email)
                user.set_password(password)
                user.save()
                return Response(data={'Success':'Password for Email ' +str(user) +' reset successful'},status=status.HTTP_200_OK)
            return Response(data = {'Error':'Email does not exists'})
        except Exception as e :
                return Response({"error" : True , "message" : str(e)},status=status.HTTP_400_BAD_REQUEST)

class PageNotFoundAPI(APIView):
    def get(self,request,*args, **kwargs):
        return Response({"error" : True, "message" : "This API Does not exists in this Application"},status=status.HTTP_404_NOT_FOUND)


