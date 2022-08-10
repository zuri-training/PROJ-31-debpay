from django import forms
from .models import*
from django.core.exceptions import ValidationError

class ContendForm(forms.ModelForm):

    class Meta:
        model = Contend
        fields = "__all__"

class HelpForm(forms.ModelForm):

    class Meta:
        model = Help
        fields = "__all__"

class DebtorForm(forms.ModelForm):

    class Meta:
        model = Debtor
        fields = "__all__"

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = "__all__"
        
        
#School registration form
class SchoolRegForm(forms.Form):
    # School_name = forms.CharField(max_length=100)
    # School_owner = forms.CharField(max_length=255)
    # Reg_number = forms.CharField(max_length=255)
    username = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    Password = forms.CharField(widget=forms.PasswordInput, min_length=5, max_length=20)
    # Confirm_password = forms.CharField(widget=forms.PasswordInput, min_length=5, max_length=20)
    
    #Validations
    # def clean_School_name(self):
    #     School_name= self.cleaned_data['School_name']
    #     if School.objects.filter(School_name__iexact=School_name).exists():
    #         raise forms.ValidationError("School already exists")
    #     return School_name
    
    def clean_email(self):
        email= self.cleaned_data['email']
        if School.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Email already exists")
        return email
    
    # def clean_School_owner(self):
    #     School_owner= self.cleaned_data['School_owner']
    #     if School.objects.filter(School_owner__iexact=School_owner).exists():
    #         raise forms.ValidationError("School_owner already exists")
    #     return School_owner
    
    # def clean_Reg_number (self):
    #     Reg_number = self.cleaned_data['Reg_number']
    #     if School.objects.filter(Reg_number__iexact=Reg_number).exists():
    #         raise forms.ValidationError("Reg_number already exists")
    #     return Reg_number  
                      
    def clean_username(self):
         username  = self.cleaned_data['username']
         if School.objects.filter(username__iexact=username).exists():
             raise forms.ValidationError("Username not available")
         return username
         
#School profile form used as an instance to update the school profile
class SchoolProfileForm(forms.ModelForm):
    class Meta:
            model = School_Profile
            fields = "__all__"  
            exclude = ['school']


#School update form
class SchoolUpdateForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['School_name','username', 'Reg_number','School_owner', 'email' ]
        
#School profile update form
class SchoolProfileUpdateForm(forms.ModelForm):
    class Meta:
            model = School_Profile
            fields = "__all__"  
            exclude = ['school']