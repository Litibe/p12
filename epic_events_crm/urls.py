from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as DRF_jwt_views

from authentication.views import UserSignUpView
from crm.views import main_page, CustomerViews

admin.site.site_header = "EpicEvents CRM"
admin.site.site_title = "EpicEvents CRM Portal"
admin.site.index_title = "Welcome to EpicEvents CRM Portal"

urlpatterns = [
     path('', main_page, name='homepage'),
     path('portal/', admin.site.urls),
     path('api/authentication/login/',
          DRF_jwt_views.TokenObtainPairView.as_view(), name='login'),
     path('api/authentication/login/refresh/',
          DRF_jwt_views.TokenRefreshView.as_view(),
          name='login_refresh'),
     path('api/authentication/signup/',
          UserSignUpView.as_view(
             {'post': "create_a_new_user"}), name='sign_up'),
     path('api/crm/customer/',
          CustomerViews.as_view(
             {'get': "read_customer"}), name='read_customer'),
     path('api/crm/customer/<id_customer>/',
          CustomerViews.as_view(
             {"get": "details_customer",
              "put": "put_customer"}), name='customer'),
]
