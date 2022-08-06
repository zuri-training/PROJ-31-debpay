from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from .forms import*
from .models import*
from django.contrib.auth import login, logout, authenticate
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User



#Just a test view to be deleted later
def contend_view(request):
    context = {}

    form = ContendForm(request.POST)

    #To check if form is valid
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "contend.html", context)

def help_view(request):
    context = {}

    form = HelpForm(request.POST)

    #To check if form is valid
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "help_page.html", context)

def debtor_form_view(request):
    context = {}

    form = DebtorForm(request.POST)

    #To check if form is valid
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "debtor_form.html", context)

def School_Register(request):

    form = SchoolRegForm()
    if request.method == 'POST':
        form = SchoolRegForm(request.POST)
        email = request.POST['email']
        username = request.POST['username']
        School_name = request.POST['School_name']
        School_owner = request.POST['School_owner']
        Reg_number = request.POST['Reg_number']
        password1 = request.POST['Password']
        password2 = request.POST['Confirm_password']
       
        
        if form.is_valid():
            if password1 == password2:
                user = School.objects.create_user(email=email, password=password1, School_name=School_name, School_owner =School_owner ,
                                                  username=username, Reg_number=Reg_number,
                        )
                user.save()
                #auth.login(request,user)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, 'School created successfully')
                return redirect('/')
          
            else:
               messages.error(request, 'password mismatch')
    else:
        form = SchoolRegForm()
    context ={'form':form}
    return render(request, 'Debtor/School_reg.html', context)

   

#Logout view for school
def School_Logout(request):
    logout(request)
    return redirect('/')
#Home page view
def land(request):
    return render(request, 'Debtor/home.html')

#School login view
def School_Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = School.objects.get(email=email)
        except:
            messages.error(request, 'user does not exist')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'user does not exist')
    return render(request, 'Debtor/School_login.html')
        
        

#School Profile update view
def School_Profile_Update(request):
    p_form = SchoolProfileUpdateForm(instance=request.user.school_profile)
    u_form = SchoolUpdateForm(instance=request.user)
    
    if request.method =='POST':
        p_form =SchoolProfileUpdateForm(request.POST,request.FILES, instance=request.user.school_profile)
        u_form = SchoolUpdateForm(request.POST,instance=request.user)
        
        if u_form.is_valid() and  p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('/')
    
    context = {'p_form': p_form, 'u_form':u_form}
    return render(request,'Debtor/Profile_Update.html', context ) 
    
    