from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from .manager import UserManager
from django.core.validators import RegexValidator

from django.core.mail import send_mail
from django.conf import settings

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    password = models.CharField(max_length=100)
    is_email_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6,null=True,blank=True)
   

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def name(self):
        return self.first_name + ' ' +self.last_name
    
    def __str__(self):
        return self.email








# Create your models here.







STATE_CHOICES = (
   ("Select","Select"),
   ("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
   ("Andhra Pradesh","Andhra Pradesh"),
   ("Arunachal Pradesh","Arunachal Pradesh"),
   ("Assam","Assam"),
   ("Bihar","Bihar"),
   ("Chhattisgarh","Chhattisgarh"),
   ("Chandigarh","Chandigarh"),
   ("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),
   ("Daman and Diu","Daman and Diu"),
   ("Delhi","Delhi"),
   ("Goa","Goa"),
   ("Gujarat","Gujarat"),
   ("Haryana","Haryana"),
   ("Himachal Pradesh","Himachal Pradesh"),
   ("Jammu and Kashmir","Jammu and Kashmir"),
   ("Jharkhand","Jharkhand"),
   ("Karnataka","Karnataka"),
   ("Kerala","Kerala"),
   ("Ladakh","Ladakh"),
   ("Lakshadweep","Lakshadweep"),
   ("Madhya Pradesh","Madhya Pradesh"),
   ("Maharashtra","Maharashtra"),
   ("Manipur","Manipur"),
   ("Meghalaya","Meghalaya"),
   ("Mizoram","Mizoram"),
   ("Nagaland","Nagaland"),
   ("Odisha","Odisha"),
   ("Punjab","Punjab"),
   ("Pondicherry","Pondicherry"),
   ("Rajasthan","Rajasthan"),
   ("Sikkim","Sikkim"),
   ("Tamil Nadu","Tamil Nadu"),
   ("Telangana","Telangana"),
   ("Tripura","Tripura"),
   ("Uttar Pradesh","Uttar Pradesh"),
   ("Uttarakhand","Uttarakhand"),
   ("West Bengal","West Bengal")
)



class Profile(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=50)

    def __str__(self):
        return self.name
    






EDUCATIONSTATE_CHOICES = (
   ("Select","Select"),
   ("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
   ("Andhra Pradesh","Andhra Pradesh"),
   ("Arunachal Pradesh","Arunachal Pradesh"),
   ("Assam","Assam"),
   ("Bihar","Bihar"),
   ("Chhattisgarh","Chhattisgarh"),
   ("Chandigarh","Chandigarh"),
   ("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),
   ("Daman and Diu","Daman and Diu"),
   ("Delhi","Delhi"),
   ("Goa","Goa"),
   ("Gujarat","Gujarat"),
   ("Haryana","Haryana"),
   ("Himachal Pradesh","Himachal Pradesh"),
   ("Jammu and Kashmir","Jammu and Kashmir"),
   ("Jharkhand","Jharkhand"),
   ("Karnataka","Karnataka"),
   ("Kerala","Kerala"),
   ("Ladakh","Ladakh"),
   ("Lakshadweep","Lakshadweep"),
   ("Madhya Pradesh","Madhya Pradesh"),
   ("Maharashtra","Maharashtra"),
   ("Manipur","Manipur"),
   ("Meghalaya","Meghalaya"),
   ("Mizoram","Mizoram"),
   ("Nagaland","Nagaland"),
   ("Odisha","Odisha"),
   ("Punjab","Punjab"),
   ("Pondicherry","Pondicherry"),
   ("Rajasthan","Rajasthan"),
   ("Sikkim","Sikkim"),
   ("Tamil Nadu","Tamil Nadu"),
   ("Telangana","Telangana"),
   ("Tripura","Tripura"),
   ("Uttar Pradesh","Uttar Pradesh"),
   ("Uttarakhand","Uttarakhand"),
   ("West Bengal","West Bengal")
)





    

class EducationLevel(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    education = models.CharField(max_length=200)
    study_field =models.CharField(max_length=200)
    university =models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state =models.CharField(choices=EDUCATIONSTATE_CHOICES,max_length=100)


    def save(self, *args, **kwargs):
        # Encrypt the fields before saving
        self.education = make_password(self.education)
        self.study_field = make_password(self.study_field)
        self.university = make_password(self.university)
        self.college = make_password(self.college)
        self.country = make_password(self.country)
        self.city = make_password(self.city)

        super(EducationLevel, self).save(*args, **kwargs)




    def __str__(self):
        return str(self.profile)


 

COURSES_CHOICES = (
    ('SELECT','SELECT'),
    ('PYTHON PROGRAMING','PYTHON PROGRAMING'),
    ('WEB DEVELOPMENT','WEB DEVELOPMENT'),
    ('DIGITAL MARKETING','DIGITAL MARKETING'),
    ('BUSSINESS MANAGEMENT','BUSSINESS MANAGEMENT'),
    ('DATA ANALYTICS','DATA ANALYTICS'),
    ('QUALITY ASSURANCE','QUALITY ASSURANCE'),

)
    
class ManageCategory(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    description = models.TextField()
    sub_category = models.CharField(max_length=100)
    category = models.CharField(choices=COURSES_CHOICES,default=None,null=True,max_length=70)
    active = models.BooleanField(default=True)
    product_image = models.ImageField(upload_to='productimg')


    def __str__(self):
        return self.title








































# class Student(models.Model):
#     f_name = models.CharField(max_length=100)
#     m_name = models.CharField(max_length=100)
#     l_name = models.CharField(max_length=100)
#     address = models.CharField(max_length=100)
#     state =models.CharField(choices=STATE_CHOICES,default=None,null=True, max_length=70)
#     city = models.CharField(max_length=100)
#     phone = models.CharField(max_length=10,validators=[RegexValidator(r'^\d{1,10}$')])
#     dob = models.DateField(null=True)
#     gender = models.CharField(choices=GENDER_CHOICES,default=None, null=True, max_length=70)
#     courses = models.CharField(choices=WEB_CHOICES,default=None,null=True, max_length=100)
    

#     def __str__(self):
#         return self.f_name
    


