from audioop import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from .forms import*
from .models import*
from django.contrib.auth import login, logout, authenticate
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import get_user_model
from django.db.models import Avg, Min, Max, Sum
from django.db.models import Q
from .filters import*
from django.contrib.auth.decorators import login_required

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


def School_Register(request):
    page = 'First'
    form = SchoolRegForm()
    if request.method == 'POST':
        form = SchoolRegForm(request.POST)
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['Password']

        password2 = request.POST['Confirm_password']
        Registered_session = request.POST['Registered_session']
        Permanent_address  = request.POST['Permanent_address']
        Founded = request.POST['Founded']
        Number_of_teachers = request.POST['Number_of_teachers']
        Contact_number = request.POST['Contact_number']
        current_address = request.POST['current_address']
        Number_of_students  = request.POST['Number_of_students']
        Session = request.POST['Session']
        
        School_owner = request.POST['School_owner']
        School_name  = request.POST['School_name']
        Reg_number = request.POST['Reg_number']



        if form.is_valid():
            if password1 == password2:
                user = School.objects.create_user(email=email, password=password1, School_name=School_name, School_owner =School_owner,
                                                  username=username, Reg_number=Reg_number,  Registered_session= Registered_session,
                                                    Permanent_address=Permanent_address,Founded=Founded, Number_of_teachers =  Number_of_teachers ,
                                                         current_address=current_address , Contact_number =  Contact_number,
                                                          Number_of_students= Number_of_students, Session=Session

)
                user.is_active = False
                user.save()
                #auth.login(request,user)
                # login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, 'School created successfully, kindly wait till the admin verify your details')
                return redirect('/')
        else:
            messages.error(request, 'password mismatch')
    else:
        form = SchoolRegForm()
    context ={'form':form, 'page':page}
    return render(request, 'Debtor/School_reg.html', context)


def ViewDebt(request):
    page ='A'
    debt = Debtor.objects.filter(
        Q(student_name__iexact=next)|
          Q(student_id__iexact=next)|
            Q(sponsor_email__iexact=next)
    ) 
    context ={'debt':debt, 'page':page ,'next': next}
    return render(request, 'Debtor/viewdebt.html', context)

def TheDebt(request):
    B = request.GET.get('b') if request.GET.get('b') !=None else''
    page = 'B'
    debt = Debtor.objects.filter( Q(student_id__iexact=B) ) 
    context ={'debt':debt, 'page': page}
    return render(request, 'Debtor/viewdebt.html', context)


def contend(request):
    form = ContendForm()
    page = 'C'
    if request.method == 'POST':
        form = ContendForm(request.POST)
        if form.is_valid():
            
            form.save()
            return redirect('/')
    context = { 'form' :form, 'page':page}
    return render(request, 'Debtor/viewdebt.html', context)
def help(request):
    return render(request, 'Debtor/help-centre.html')

def About_us(request):
    return render(request, 'Debtor/About-us.html')

def FAQs(request):
    searcher = request.GET.get("q") if request.GET.get("q") !=None else""
    help = Help.objects.filter(Q (title__icontains=searcher)|
                               Q (body__icontains=searcher))
    context = {'help':help, 'searcher':searcher}
    return render(request, 'FAQs.html', context)

def Contact(request):
    return render(request, 'Debtor/contact_us.html')

#Logout view for school
def School_Logout(request):
    logout(request) 
    return redirect('/')
#Home page view
def land(request):
    return render(request, 'Debtor/home.html')

#Privacy & Policy page view
def Privacy(request):
    return render(request, 'Privacypolicy.html')


#FAQs page view
def faqs(request):
    return render(request, 'FAQs.html')


#School login view
def Auth_School(request):
    if request.user.is_authenticated:
        return redirect ('/')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            try:
                user = School.objects.get(email=email)
            except:
                messages.error(request, 'user does not exist')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('dashboard')
            else:
                messages.error(request, 'user does not exist')

        return render(request, 'Debtor/login.html')
            

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
    


def dash (request):
    run = request.GET.get('test') if request.GET.get('test') !=None else''
    fork = Post.objects.filter(Q(title__icontains=run)|
                               Q(body__icontains=run))
    page ='dash'
    goat = fork.count()
    context ={'fork':fork, 'page':page, 'goat':goat }
    return render(request, 'Debtor/profile.html', context) 

@login_required
def dashboard(request):
    user_contend = Contend.objects.filter(school=request.user)
    lost =School_Profile.objects.all() 
    local = Locality.objects.all()
    page = 'home'
    meet = Meeting.objects.filter(meeting_host=request.user)
    post = Post.objects.all() [:5]
    
    loin = post.count()
    debtor = Debtor.objects.filter(school = request.user).aggregate( Total_Debt = Sum('debt'))
    post_mine = Post.objects.filter(school_post = request.user).count()
    debtors = Debtor.objects.filter(school = request.user).count()
    debtor_list = Debtor.objects.filter(school = request.user).count()
    post.image = request.FILES
    context ={'page':page , 'meet':meet ,'local':local ,'lost':lost , 'debtor_list':debtor_list, 'mine':post_mine, 'post':post, 'debtors':debtors, 'debtor': debtor}
    return render(request, 'Debtor/profile.html', context)


def Create_Chat(request):
    page = 'Chat'
    form = ChatForm()
    if request.method =='POST':
        form = ChatForm(request.POST, request.FILES)
        if form.is_valid:
            room = form.save(commit=False)
            room.sender = request.user
            room.save()
            return redirect('Chat_All')
    
    context = {'form':form, 'page':page}
    return render(request, 'Debtor/profile.html', context)

def Chat_All(request):
    chat_all = School_Chat.objects.filter(sender = request.user)
    sec_chat = School_Chat.objects.filter(recepient = request.user)
    page ='Chat_All'
    context ={'page':page, 'sec_chat':sec_chat, 'chat_all':chat_all}
    return render(request, 'Debtor/profile.html', context)

def Chat_List(request, pk):
    chat = School_Chat.objects.get(id=pk)
    page = 'Chat_List'
    
    context ={'chat':chat, 'page':page}
    return render(request, 'Debtor/profile.html', context)

def Contendant(request):
    page = 'contendant'
    user_contend = Contend.objects.filter(school=request.user)
    context = {'user_contend':user_contend, 'page':page}
    return render(request, 'Debtor/profile.html', context)


def CreatePost(request):
    page = 'post'
    form  =  PostCreateForm()
    if request.method == 'POST':
         form  =  PostCreateForm(request.POST, request.FILES)
         if form.is_valid():
            room = form.save(commit=False)
            room.school_post = request.user
            room.save()
            return redirect('dashboard')
    else:
        form = PostCreateForm()
        
    context ={'form':form, 'page':page}
    return render(request, 'Debtor/profile.html', context)


def post_list(request, pk):
    page = 'list'
    post = Post.objects.get(id=pk)
    post_comment = post.comment_set.all()
    if request.method == 'POST':
        post_comment = Comment.objects.create(
            school = request.user,
            post = post,
            body = request.POST.get('body')
        )
        return redirect('list', pk=post.id)
    
    context = {'post':post, 'post_comment':post_comment, 'page':page}
    
    return render(request, 'Debtor/profile.html', context)


def Post_all(request):
    searcher = request.GET.get("search_post") if request.GET.get("search_post") !=None else""
    post_search = Post.objects.filter(title__icontains=searcher) 
    # post_search = Post.objects.filter(title__icontains=searcher)
    post = Post.objects.all()
    total_post = post.count()
    my_filter = PostFilter(request.GET, queryset=post)
    post = my_filter.qs
    partial_count = post.count()
    page = 'all'
    context ={'post':post, 'partial_count':partial_count , 'my_filter': my_filter, 'post_search':post_search, 'searcher':searcher, 'total_post': total_post, 'page':page}
    return render(request, 'Debtor/profile.html', context)
 
 
def AllSchool(request):
    page = 'all_school'
    all_school_profile = School_Profile.objects.all()
    school_list = SchoolFilter(request.GET,  queryset=all_school_profile)
    all_school_profile = school_list.qs
    context = { 'all_school_profile': all_school_profile, 'school_list':school_list, 'page':page,}
    return render(request, 'Debtor/profile.html', context)  

def OneSchool(request, pk):
    page ='one_school'
    one_school = School.objects.get(School_id=pk)
    one_school_debtor = Debtor.objects.filter(school=one_school)
    one_school_debt = Debtor.objects.filter(school=one_school).aggregate(Total_Debt = Sum('debt'))
    context = {'page':page, 'one_school_debt':one_school_debt , 'one_school_debtor':one_school_debtor, 'one_school':one_school} 
    return render(request, 'Debtor/profile.html', context)


def  postUpd(request, pk):
    page = 'upd'
    post = Post.objects.get(id=pk)
    form  =  PostForm(instance = post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance= post)
        if form.is_valid:
            form.save()
            return redirect('dashboard')
    context ={'form':form, 'page':page}
    return render(request, 'Debtor/profile.html', context)


def postDel(request, pk):
    page ='del'
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('dashboard')
    

def debtor_reg(request):
    form = DebtorForm()
    if request.method == 'POST':
        form = DebtorForm(request.POST, request.FILES)
        if form.is_valid():
            room = form.save(commit=False)
            room.school = request.user
            room.save()
            return redirect('dashboard')
    else:
        form = DebtorForm()
        messages.error (request, 'invalid form input')
    context = {'form':form}
    return render(request, "Debtor/debtor_form.html", context)
        

# def debtor_upd(request, pk):
#     page = 'update'
#     debtor = Debtor.objects.get(id=pk)
#     form = DebtorUpdateForm(instance=debtor)
#     if request.method == 'POST':
#         form = DebtorForm(request.POST, request.FILES, instance=debtor)
#         if form.is_valid():
#             room = form.save(commit=False)
#             room.school = request.user
#             room.save()
#             return redirect('debt')
 
#     context = {'form':form, 'page':page}
#     return render(request, "Debtor/debtor_form.html", context)

def user_debtor(request):
    school_debtors = Debtor.objects.filter(school = request.user)
    total_debtors =  school_debtors.count()
    total_debt =   school_debtors.aggregate(Total_debt = Sum('debt'))
    page = 'debt'
    context = {'school_debtors':school_debtors, 'total_debt':total_debt , 'total_debtors':total_debtors , 'page':page}
    return render(request, 'Debtor/profile.html', context)
    
def one_debtor(request, pk):
    debtor = Debtor.objects.get(id=pk)
    post = Post.objects.filter(deptors_list = debtor)
    page = 'one'
    context = {'debtor':debtor, 'post':post ,'page':page}
    return render(request, 'Debtor/profile.html', context)
    
    
def debtor_delete(request,pk):
    debtor = Debtor.objects.get(id=pk).delete()
    return redirect('debt')

def debtor_all(request):
    debtor = Debtor.objects.all()
    total_debtor = debtor.count()
    debtor_filter = DebtorFilter(request.GET, queryset=debtor)
    debtor = debtor_filter.qs
    page ='throw'
    context = {'page':page,  'debtor_filter':debtor_filter , 'total_debtor':total_debtor, 'debtor':debtor}
    return render(request, 'Debtor/profile.html', context)


def CreateMeeting(request):
    form =MeetingCreationForm()
    page = 'meeting'
    if request.method == 'POST':
        form = MeetingCreationForm(request.POST, request.FILES)
        if form.is_valid():
            room = form.save(commit = False)
            room.meeting_host = request.user
            room.save()
            return redirect('dashboard')
    
    context = {'page':page, 'form':form}
    return render(request, 'Debtor/profile.html', context)


def Total_meeting(request):
    page = 'Total_meeting'
    meeting = Meeting.objects.all()
    context = {'page':page, 'meeting':meeting}
    return render(request, 'Debtor/profile.html', context)


def A_meeting(request, pk):
    meeting = Meeting.objects.get(id=pk)
    page = 'A_meeting'
    context = {'page':page, 'meeting':meeting}
    return render(request, 'Debtor/profile.html', context)
    
    
def EachMeeting(request, pk):
    page = 'each_meeting'
    one_meeting = Meeting.objects.get(id=pk)

    meeting_comment = Meeting_Comment.objects.filter(meeting = one_meeting)
    form =  MeetingCommentForm()
    if request.method == 'POST':
        form =  MeetingCommentForm(request.POST, request.FILES)
        if form.is_valid():
            room = form.save(commit=False)
            room.attendee = request.user
            room.meeting =  one_meeting
        
            room.save()
            
            return redirect('EachMeeting', one_meeting.id)
        
    else:
         form =  MeetingCommentForm()        
    context = {'one_meeting':one_meeting, 'meeting_comment':meeting_comment , 'form':form , 'page': page}
    return render(request, 'Debtor/profile.html', context)

def EachComment(request, pk):
    page = 'each_comment'
    each_comment = Meeting_Comment.objects.get(id=pk)
    each_comment_reply = each_comment.meeting_comment_reply_set.all()
    rep_m =  Meeting_Comment_Reply.objects.filter(comment = each_comment)
    if request.method == 'POST':
        each_comment_reply =  Meeting_Comment_Reply.objects.create(
            body = request.POST.get('body'),
            image = request.FILES.get('image'),
            responder = request.user,
            comment = each_comment,
           )
        return redirect('EachComment', each_comment.id)
 
    context ={'page':page, 'each_comment':each_comment, 'rep_m': rep_m, 'each_comment':each_comment, 'each_comment_reply': each_comment_reply }
    return render(request, 'Debtor/profile.html', context)


def ReplyComment(request, pk):
    page = 'reply'
    commented = Comment.objects.get(id=pk)
    comment_reply = commented.reply_set.all()
    if request.method == 'POST':
        comment_reply = Reply.objects.create(
        school = request.user,
        comment = commented,
        body = request.POST.get('reply_body')    
        )
        return redirect('ReplyComment', commented.id)
        
    context = {'comment_reply': comment_reply, 'page':page,'commented':commented}
    return render(request, 'Debtor/profile.html', context)


def MeetingUpdate(request, pk):
    meet = Meeting.objects.get(id=pk)
    form = MeetingUpdateForm(instance=meet)
    page = 'meeting_update'
    if request.method == 'POST':
        form = MeetingUpdateForm(request.POST, request.FILES, instance=meet)
        if form.is_valid():
            room = form.save(commit=False)
            room.meeting_host = request.user
            room.save()
            return redirect('EachMeeting', meet.id)
    else:
        form = MeetingUpdateForm(instance=meet)
    context = {'form':form, 'page':page ,'meet':meet}
    return render(request, 'Debtor/profile.html', context)

def debtor_upd(request, pk):
    page = 'update'
    debtor = Debtor.objects.get(id=pk)
    form = DebtorUpdateForm(instance=debtor)
    if request.method == 'POST':
        form = DebtorForm(request.POST, request.FILES, instance=debtor)
        if form.is_valid():
            room = form.save(commit=False)
            room.school = request.user
            room.save()
            return redirect('debt')
 
    context = {'form':form, 'page':page}
    return render(request, "Debtor/debtor_form.html", context)

