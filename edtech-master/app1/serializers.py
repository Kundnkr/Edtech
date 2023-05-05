from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from .models import User,Profile,ManageCategory,EducationLevel
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import default_token_generator
from rest_framework.exceptions import ValidationError


from django.contrib.auth.tokens import PasswordResetTokenGenerator 
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from xml.dom import ValidationErr
from django.utils.encoding import smart_str,force_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from app1.utils import Util
import smtplib

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','phone','password','is_email_verified','confirm_password')


    def validate(self,data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("The Password does not match")
        return data
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create(
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            phone = validated_data['phone'],

        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    

class loginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()


    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
    

class PasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()



class VerifyAccountSerializer(serializers.Serializer):
     email = serializers.EmailField()
     otp = serializers.CharField()








class SendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        fields = ['email']

    def validate(self,attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user= User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print("Enocded UID",uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print('Password Reset Token',token)
            link = 'http://localhost:3000/api/user/reset/'+uid+'/'+token
            print('Password Reset Link',link)
            # Send Email
            body = 'Click Following Link to Reset Your Password' + link
            data = {
                'subject':'Reset Your Password',
                'body':body,
                'to_email':user.email 

            }
            Util.send_email(data)
            return attrs
        else:
            raise ValidationErr('You are not a Registered User')
        return super().validate(attrs)
    

class UserPasswordRestSerializer(serializers.Serializer):
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            confirm_password = attrs.get('confirm_password')
            uid = self.context.get('uid')
            token = self.context.get('token')

            if password != confirm_password:
                raise serializers.ValidationError('Password and Confirm Password doesnot match')
            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user,token):
                raise ValidationErr('Token is not Valid or Expired')
        
            user.set_password(password)
            user.save()
            return attrs

        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user,token)
            raise ValidationErr('Token is not valid or Expired')
        




class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user','name','locality','city','state','zipcode']


class ManageCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ManageCategory
        fields =('title','selling_price','description','category','active','product_image')


class EducationLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationLevel
        fields =('profile','education','study_field','university','college','country','city','state')

    




# class StudentSerializer(serializers.ModelSerializer):
#     #dob = serializers.DateField(format="%d-%m-%Y")
#     class Meta:
#         model = Student
#         fields = ('f_name','l_name','m_name','address','city','gender','courses')

#     def create(self, validated_data):
#         validated_data['f_name'] = make_password(validated_data['f_name'])
#         validated_data['l_name'] = make_password(validated_data['l_name'])
#         validated_data['m_name'] = make_password(validated_data['m_name'])
#         validated_data['address'] = make_password(validated_data['address'])
#        # validated_data['phone'] = make_password(validated_data['phone'])
#        # validated_data['dob'] = make_password(validated_data['dob'])
#         validated_data['gender'] = make_password(validated_data['gender'])
#         validated_data['courses'] = make_password(validated_data['courses'])
#         return super().create(validated_data)
    


