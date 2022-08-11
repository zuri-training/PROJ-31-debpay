from django.urls import path, include
from .views import contend_view, help_view # Delete ModelView  debtor_form_view 
from Debtor import views
urlpatterns = [
    path('contend', contend_view, name='home'),
    path('help/', help_view, name='help'),
    # path('debtor_reg/', debtor_form_view, name='debtor_reg'),
    
    
    #Default authentication home
    path('', views.land, name='land'), 

    path('dashboard', views.dashboard, name='dashboard'),
    path('register', views.School_Register, name='register'),
    path('logout', views.School_Logout, name='logout'),
    path('login', views.School_Login, name='login'),
    path('post_create', views.CreatePost, name='post_create'),
    path('debtor', views.debtor_reg, name='debtor_reg'),
    path('list/<str:pk>', views.post_list, name='list'),
    path('upd/<str:pk>', views.postUpd , name='upd'),
    path('Post_all', views.Post_all, name='Post_all'),
    path('debt', views.user_debtor, name='debt'),
    path('each_debtor/<str:pk>', views.one_debtor, name='each_debtor'),
    path('del/<str:pk>', views.postDel , name='del'),
    path('debtor_delete/<str:pk>', views.debtor_delete, name='debtor_delete'),
    path('debtor_all', views.debtor_all, name="debtor_all"),
    path('debtor_upd/<str:pk>', views.debtor_upd, name='debtor_upd'),
    # path('accounts/', include('django.contrib.auth.urls')),#Django built-in authentication system
    path('School_Profile_Update', views.School_Profile_Update, name='School_Profile_Update'), 
    path('ReplyComment/<str:pk>', views.ReplyComment, name="ReplyComment"),
    path('AllSchool', views.AllSchool, name='AllSchool'),
    path('OneSchool/<str:pk>', views.OneSchool, name='OneSchool'),
    
    path("CreateMeeting", views.CreateMeeting, name="CreateMeeting"),
    path('EachMeeting/<str:pk>', views.EachMeeting, name="EachMeeting"),
    path('EachComment/<str:pk>', views.EachComment, name="EachComment"),
    path('MeetingUpdate/<str:pk>', views.MeetingUpdate, name='MeetingUpdate')
 


    #path('post/', debtor_form_view, name='post')
]

