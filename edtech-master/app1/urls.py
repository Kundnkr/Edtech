from django.urls import path,re_path

from app1.views import login_view,change_password_view,RegisterAPI,SendPasswordResetEmailView,UserPasswordRestView,VerifyOTP,ProfileView,ManageCategoryView,EducationView,PythonAPIView,WebDevelopmentAPIView,DigitalMarketingAPIView,BusinessManagementAPIView,DataAnalyticsAPIView,QualityAssuranceAPIView

urlpatterns = [
   # path('std/<int:pk>/',StudentDetail.as_view(),name='StudentDetail'),
   # path('std-create/',StudentCreate.as_view(),name='StudentCreate'),
    path('register/',RegisterAPI.as_view(),name='RegisterView'),
    path('verify/',VerifyOTP.as_view(),name='verify'),
    path('login/',login_view, name='login'),
    path('change-password/',change_password_view, name='change_password'),
    path('send-reset-password-email/',SendPasswordResetEmailView.as_view(),name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/',UserPasswordRestView.as_view(),name='reset-password'),
    path('profile/',ProfileView.as_view(),name='profilte'),
    path('manage-category/<int:pk>/activation/',ManageCategoryView.as_view(),name='manage-category'),
    path('python/<slug:data>',PythonAPIView.as_view(),name='python'),
    path('development/<slug:data>',WebDevelopmentAPIView.as_view(),name='development'),
    path('digital/<slug:data>',DigitalMarketingAPIView.as_view(),name='digital'),
    path('management/<slug:data>',BusinessManagementAPIView.as_view(),name='management'),
    path('analytics/<slug:data>',DataAnalyticsAPIView.as_view(),name='analytics'),
    path('quality/<slug:data>',QualityAssuranceAPIView.as_view(),name='quality'),
    path('education/',EducationView.as_view(),name='education'),


  
]




