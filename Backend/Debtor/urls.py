from django.urls import path
from .views import contend_view, help_view, debtor_form_view # Delete ModelView

urlpatterns = [
    path('', contend_view, name='home'),
    path('help/', help_view, name='help'),
    path('debtor_reg/', debtor_form_view, name='debtor_reg'),
    path('post/', debtor_form_view, name='post')
]

