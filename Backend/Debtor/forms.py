from django import forms
from .models import*
from django.core.exceptions import ValidationError

# class ContendForm(forms.ModelForm):

#     class Meta:
#         model = Contend
#         fields = "__all__"

class ContendForm(forms.ModelForm):
    class Meta:
        model = Contend
        fields = "__all__"
class HelpForm(forms.ModelForm):

    class Meta:
        model = Help
        fields = "__all__"

class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = "__all__"
        exclude =['school_post', ]
        
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = "__all__"
        exclude =['school_post', ]

class DebtorForm(forms.ModelForm):
    class Meta:
        model = Debtor
        fields = '__all__'
        exclude = ['school', ]        


class DebtorUpdateForm(forms.ModelForm):
    class Meta:
        model = Debtor
        fields = '__all__'
        exclude = ['school', ]   
 
 

# class SchoolRegForm(forms.Form):
#     School_name = forms.CharField(max_length=100)
#     username = forms.CharField(max_length=255)
#     email = forms.EmailField(max_length=255)
#     Password = forms.CharField(widget=forms.PasswordInput, min_length=5, max_length=20)
#     Confirm_password = forms.CharField(widget=forms.PasswordInput, min_length=5, max_length=20)        


# School registration form
class SchoolRegForm(forms.Form):
    School_name = forms.CharField(max_length=100)
    School_owner = forms.CharField(max_length=255)
    Reg_number = forms.CharField(max_length=255)
    username = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    Registered_session = forms.CharField(max_length=255) 
    current_address = forms.CharField(max_length=255)  
    Permanent_address = forms.CharField(max_length=255)         
    Number_of_teachers = forms.IntegerField()
    Contact_number = forms.IntegerField()
    Number_of_students = forms.IntegerField()
    Founded = forms.CharField(max_length=100)
    Session = forms.CharField(max_length=100)
    Password = forms.CharField(widget=forms.PasswordInput, min_length=5, max_length=20)
    Confirm_password = forms.CharField(widget=forms.PasswordInput, min_length=5, max_length=20)

 

    
    #Validations
    def clean_School_name(self):
        School_name= self.cleaned_data['School_name']
        if School.objects.filter(School_name__iexact=School_name).exists():
            raise forms.ValidationError("School already exists")
        return School_name
    
    def clean_email(self):
        email= self.cleaned_data['email']
        if School.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Email already exists")
        return email
    
    def clean_username(self):
         username  = self.cleaned_data['username']
         if School.objects.filter(username__iexact=username).exists():
             raise forms.ValidationError("Username not available")
         return username
     
    def clean_Reg_number(self):
        Reg_number  = self.cleaned_data['Reg_number']
        if School.objects.filter(Reg_number__iexact=Reg_number).exists():
             raise forms.ValidationError("The Reg_number inputed is already in use")
        return  Reg_number
    
    def clean_School_owner(self):
        School_owner  = self.cleaned_data['School_owner']
        if School.objects.filter(School_owner__iexact=School_owner).exists():
             raise forms.ValidationError("You have a school already")
        return School_owner
    
        
    # def clean_Phone_number(self):
    #     Phone_number  = self.cleaned_data['Phone_number']
    #     if School.objects.filter(Phone_number__iexact=Phone_number).exists():
    #          raise forms.ValidationError("Phone number belong to another user ")
    #     return Phone_number
         
          
#School profile form used as an instance to update the school profile
class SchoolProfileForm(forms.ModelForm):
    class Meta:
            model = School_Profile
            fields = "__all__"  
            exclude = ['school']


class SchoolUpdateForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['School_name','username', 'email',  ]
# #School update form
# class SchoolUpdateForm(forms.ModelForm):
#     class Meta:
#         model = School
#         fields = ['School_name','username', 'current_address', 
#                   'Number_of_teachers' , 'Founded', 'Number_of_students', 
#                   'current_address', 'Permanent_address' ,'Phone_numnber',
#                   'Reg_number','School_owner', 'email', 'Registered_session', ]
       
    
        
#School profile update form
class SchoolProfileUpdateForm(forms.ModelForm):
    class Meta:
            model = School_Profile
            fields = "__all__"  
            exclude = ['school',]
            
            
            
class MeetingCreationForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['title', 'description', 'meeting_profile_image']
        
class MeetingUpdateForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = "__all__"
        exclude = ['meeting_host', ]
        

class MeetingCommentForm(forms.ModelForm):
    class Meta:
        model = Meeting_Comment
        fields = "__all__"
        exclude = ['updated', 'created', 'attendee', 'meeting' ]
        
        
        
class ChatForm(forms.ModelForm):
    class Meta:
        model = School_Chat
        fields = "__all__"
        exclude = ['sender', ]
        
        
        
            
