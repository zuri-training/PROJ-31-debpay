from django.urls import path, include
from .views import contend_view, help_view # Delete ModelView  debtor_form_view 
from Debtor import views
urlpatterns = [
    path('contend', contend_view, name='home'),
    path('help/', help_view, name='help'),
    # path('debtor_reg/', debtor_form_view, name='debtor_reg'),
    
    path('help', views.help, name='help'),
    path('Privacy', views.Privacy, name='Privacy'),
    path('About_us', views.About_us, name='About_us'),
    path('FAQs', views.FAQs, name='FAQs'),
    #Default authentication home

    # path('', views.land, name='land'), 
    
   
    path('', views.land, name='land'),
    path('Create_Chat', views.Create_Chat, name='Create_Chat'),
    path('Chat_List/<str:pk>', views.Chat_List, name='Chat_List'),
    path('Chat_All', views.Chat_All, name='Chat_All'),
    # path('FAQs', views.FAQs, name='FAQs'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('register', views.School_Register, name='register'),
    path('Contact', views.Contact, name='Contact'),
    path('ViewDebt', views.ViewDebt, name='ViewDebt'),
    path('TheDebt', views.TheDebt, name='TheDebt'),
    path('Total_meeting', views.Total_meeting, name='Total_meeting'),
    path('A_meeting/<str:pk>', views.A_meeting, name='A_meeting'),
    path('Contend', views.contend, name='Contend'),
    path('Contendant', views.Contendant, name='Contendant'),
    path('logout', views.School_Logout, name='logout'),
    path('Auth_School', views.Auth_School, name='Auth_School'),
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
    path('accounts/', include('django.contrib.auth.urls')),#Django built-in authentication system
    path('School_Profile_Update', views.School_Profile_Update, name='School_Profile_Update'), 
    path('ReplyComment/<str:pk>', views.ReplyComment, name="ReplyComment"),
    path('AllSchool', views.AllSchool, name='AllSchool'),
    path('OneSchool/<str:pk>', views.OneSchool, name='OneSchool'),
    
    path("CreateMeeting", views.CreateMeeting, name="CreateMeeting"),
    path('EachMeeting/<str:pk>', views.EachMeeting, name="EachMeeting"),
    path('EachComment/<str:pk>', views.EachComment, name="EachComment"),
    path('MeetingUpdate/<str:pk>', views.MeetingUpdate, name='MeetingUpdate'),
    path('dash', views.dash, name='dash')
 


    #path('post/', debtor_form_view, name='post')
]

