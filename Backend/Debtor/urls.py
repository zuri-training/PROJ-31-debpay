from django.urls import path, include
from .views import contend_view, help_view, debtor_form_view # Delete ModelView
from Debtor import views
urlpatterns = [
    path('contend', contend_view, name='home'),
    path('help/', help_view, name='help'),
    path('debtor_reg/', debtor_form_view, name='debtor_reg'),
    
    
    #Default authentication home
    path('', views.land, name='land'), 
    path('register/', views.School_Register, name='register'),
    path('logout/', views.School_Logout, name='logout'),
    path('login/', views.School_Login, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),#Django built-in authentication system
    path('School_Profile_Update', views.School_Profile_Update, name='School_Profile_Update'), 

    #path('post/', debtor_form_view, name='post')
]

