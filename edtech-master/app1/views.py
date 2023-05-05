from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User,Profile,ManageCategory,EducationLevel
from rest_framework import generics, permissions, status,serializers
from app1.serializers import UserSerializer,loginSerializer,PasswordSerializer,SendPasswordResetEmailSerializer,UserPasswordRestSerializer,VerifyAccountSerializer,ProfileSerializer,ManageCategorySerializer,EducationLevelSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.http import Http404
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from rest_framework.views import APIView

from .emails import *


# Create your views here.

# class RegisterView(generics.CreateAPIView):
#     #renderer_classes = [UserRenderer]          #
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class RegisterAPI(APIView):
    def post(self,request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            send_otp_via_email(serializer.data['email'])
            return Response({'status':200,'msg':'Registration is Successfully','data':serializer.data})
        return Response({'status':400,'msg':'Something went Wrong','data':serializer.errors})
    



class VerifyOTP(APIView):
    def post(self,request):
        try:
            data = request.data
            serializer = VerifyAccountSerializer(data=data)
            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data ['otp']
                user= User.objects.filter(email= email,otp=otp)
                if not user.exists():
                    return Response({'status':400,'msg':'Something went Wrong','data':'Invalid Email'})
                if user[0].otp != otp:
                    return Response({'status':400,'msg':'Something went Wrong','data':'wrong otp'})
                user = user.first()
                user.is_email_verified = True
                user.save()
                return Response({'status':200,'msg':'account verified','data':{}})
            return Response({'status':400,'msg':'Something went Wrong','data':serializer.errors})
        except Exception as e:
            print(e)


    












@api_view(['POST'])
def login_view(request):
    serializer = loginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'status':200,'msg':'Login Successfully','token': token.key})
    return Response({'status':400,'msg':'Something went Wrong',"data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def logout_view(request):
    logout(request)
    return Response({'message': 'Logged out successfully'})


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def change_password_view(request):
    serializer = PasswordSerializer(data=request.data)
    if serializer.is_valid():
        user = request.user
        old_password = serializer.data.get('old_password')
        new_password = serializer.data.get('new_password')
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response({'message': 'Password changed successfully'})
        return Response({'message': 'Invalid old password'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class SendPasswordResetEmailView(APIView):
    #renderer_classes = [UserRenderer]
    def post(self,request,format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Reset Link send.Please check your Email'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class UserPasswordRestView(APIView):
    def post(self,request,uid,token,format=None):
        serializer = UserPasswordRestSerializer(data=request.data,context={'uid':uid,'token':token})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Passowrd Reset Successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




class EducationView(generics.CreateAPIView):
    queryset = EducationLevel.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = EducationLevelSerializer




# class StudentCreate(generics.CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer



# class StudentDetail(generics.RetrieveAPIView):
#     serializer_class = StudentSerializer
#     queryset = Student.objects.all()
#     lookup_field = 'pk'

    # def get(self, request,pk, *args, **kwargs):
        
    #     instance = self.get_object(pk=pk)
    #     serializer = self.get_serializer(instance)
    #     details = serializer.data['encrypted_details']
    #     decrypted_details = {}
    #     for key, value in details.items():
    #         decrypted_details[key] = check_password(value, '')
    #     serializer.data['encrypted_details'] = decrypted_details
    #     return Response(serializer.data)


class ProfileView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer


class ManageCategoryView(APIView):
    def patch(self, request, pk):
        try:
            product = ManageCategory.objects.get(pk=pk)
        except ManageCategory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ManageCategorySerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class PythonAPIView(APIView):
    def get(self, request, data=None):
        if data == None:
            python = ManageCategory.objects.filter(category='PYTHON PROGRAMING')
        elif data == 'DataScience' or data == 'MachineLearning' or data == 'Webdevelopment' or data == 'Pythonprograming':
            python = ManageCategory.objects.filter(category='PYTHON PROGRAMING').filter(sub_category=data)
        elif data == 'below':
            python = ManageCategory.objects.filter(category='PYTHON PROGRAMING', selling_price__lt=3000)
        elif data == 'above':
            python = ManageCategory.objects.filter(category='PYTHON PROGRAMING', selling_price__gt=3000)
        serializer = ManageCategorySerializer(python, many=True)
        return Response(serializer.data)
    

class WebDevelopmentAPIView(APIView):
    def get(self, request, data=None):
        if data == None:
            webdevelopment = ManageCategory.objects.filter(category='WEB DEVELOPMENT')
        elif data == 'Django' or data == 'React' or data == 'WordPress' or data == 'PHP':
            webdevelopment = ManageCategory.objects.filter(category='WEB DEVELOPMENT').filter(sub_category=data)
        elif data == 'below':
            webdevelopment = ManageCategory.objects.filter(category='WEB DEVELOPMENT', selling_price__lt=5000)
        elif data == 'above':
            webdevelopment = ManageCategory.objects.filter(category='WEB DEVELOPMENT', selling_price__gt=5000)
        serializer = ManageCategorySerializer(webdevelopment, many=True)
        return Response(serializer.data)
    

class DigitalMarketingAPIView(APIView):
    def get(self, request, data=None):
        if data == None:
            digitalmarketing = ManageCategory.objects.filter(category='DIGITAL MARKETING')
        elif data == 'SEO' or data == 'SEM' or data == 'SMM' or data == 'Display':
            digitalmarketing = ManageCategory.objects.filter(category='DIGITAL MARKETING').filter(sub_category=data)
        elif data == 'below':
            digitalmarketing = ManageCategory.objects.filter(category='DIGITAL MARKETING', selling_price__lt=5000)
        elif data == 'above':
            digitalmarketing = ManageCategory.objects.filter(category='DIGITAL MARKETING', selling_price__gt=5000)
        serializer = ManageCategorySerializer(digitalmarketing, many=True)
        return Response(serializer.data)
    
class BusinessManagementAPIView(APIView):
    def get(self, request, data=None):
        if data == None:
            businessmanagement = ManageCategory.objects.filter(category='BUSSINESS MANAGEMENT')
        elif data == 'Marketing' or data == 'Sales' or data == 'Finance':
            businessmanagement = ManageCategory.objects.filter(category='BUSSINESS MANAGEMENT').filter(sub_category=data)
        elif data == 'below':
            businessmanagement = ManageCategory.objects.filter(category='BUSSINESS MANAGEMENT',selling_price__lt=5000)
        elif data == 'above':
            businessmanagement = ManageCategory.objects.filter(category='BUSSINESS MANAGEMENT',selling_price__gt=5000)
        serializer = ManageCategorySerializer(businessmanagement, many=True)
        return Response(serializer.data)
    
    
class DataAnalyticsAPIView(APIView):
    def get(self, request, data=None):
        if data == None:
            dataanalytics = ManageCategory.objects.filter(category='DATA ANALYTICS')
        elif data == 'Tableau' or data == 'PowerBI':
            dataanalytics = ManageCategory.objects.filter(category='DATA ANALYTICS').filter(sub_category=data)
        elif data == 'below':
            dataanalytics = ManageCategory.objects.filter(category='DATA ANALYTICS',selling_price__lt=5000)
        elif data == 'above':
            dataanalytics = ManageCategory.objects.filter(category='DATA ANALYTICS',selling_price__gt=5000)
        serializer = ManageCategorySerializer(dataanalytics,many=True)
        return Response(serializer.data)
    
    
class QualityAssuranceAPIView(APIView):
    def get(self, request, data=None):
        if data == None:
            quality = ManageCategory.objects.filter(category='QUALITY ASSURANCE')
        elif data == 'SoftwareTesting' or data == 'TestAutomation':
            quality = ManageCategory.objects.filter(category='QUALITY ASSURANCE').filter(sub_category=data)
        elif data == 'below':
            quality = ManageCategory.objects.filter(category='QUALITY ASSURANCE',selling_price__lt=5000)
        elif data == 'above':
            quality = ManageCategory.objects.filter(category='QUALITY ASSURANCE',selling_price__gt=5000)
        serializer = ManageCategorySerializer(quality,many=True)
        return Response(serializer.data)
    