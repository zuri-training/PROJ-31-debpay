import django_filters
from .models import*
from django_filters import CharFilter

class PostFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains',label='title')
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ['image', 'body', 'created', 'title', 'updated']
class FirstPostFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains',label='Title')
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ['image', 'body', 'created', 'school_post' , 'title','updated', 'deptors_list']

        
class SchoolFilter(django_filters.FilterSet):
    class Meta:
        model= School_Profile
        fields = ['locality', ]    

class DebtorFilter(django_filters.FilterSet):
    student_name = CharFilter(field_name='student_name', lookup_expr='icontains', label='Student')
    class Meta:
        model = Debtor
        fields = [ 'student_id', 'debt']
        
        
        
class HelpFilter(django_filters.FilterSet):
    class Meta:
        model = Help
        fields = "__all__"
        
        

class DebtorFilter(django_filters.FilterSet):
    class Meta:
        model = Debtor
        fields = ['student_name', 'student_id', 'sponsor_email']     
        