from django.db import models
from django.utils import timezone
from shortuuid.django_fields import ShortUUIDField
from django.contrib.auth.models import AbstractUser

class Locality (models.Model):
    country = models.CharField(max_length=100)
    ctate = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    local_government = models.CharField(max_length=100)
    
    def __str__(self):
        return self.local_government

class School (AbstractUser):
    School_owner = models.CharField(max_length=255, null=True)
    School_name = models.CharField(max_length=255)
    School_id = ShortUUIDField(
        length= 4,
        max_length = 10,
        prefix = 'DP',
        alphabet = "123456efghij",
        primary_key = True
    )
    Reg_number = models.CharField(max_length=255, null=True)  
    Registered_session = models.CharField(max_length=255, null=True)  
    current_address = models.CharField(max_length=255, null=True)  
    Permanent_address = models.CharField(max_length=255, null=True)         
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    Number_of_teachers = models.IntegerField(null=True)
    Contact_number = models.IntegerField(null=True)
    Number_of_students = models.IntegerField(null=True)
    Founded = models.CharField(max_length=100, null=True)
    Session = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    
  
    def __str__(self):
        return self.School_name


class UserVerification(models.Model):
    name = models.OneToOneField(School, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        ordering = ['-created', ]
        
    def __str__(self):
        return f' {self.name} user verification'
    
    
    
class School_Profile (models.Model):
    school = models.OneToOneField(School, on_delete=models.CASCADE)
    profile_pics = models.ImageField(default='fixed.png', upload_to='profile_pics')
    School_owner_pics = models.ImageField(default='fixed.jpg', upload_to='school_owner_pics', null=True)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE,  blank=True, null=True)
    
    def __str__(self):
        return f'{self.school.School_name} Profile'
    




class Debtor (models.Model):
    student_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100)
    sponsor_email = models.EmailField(max_length=100, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    sponsor_relationship = models.CharField(max_length=50)
    sponsor_name = models.CharField(max_length=255)
    sponsor_location = models.CharField(max_length=255)
    debtor_image = models.ImageField(upload_to='debtors pics',default='fixed.jpg', null=True)
    debt = models.IntegerField()
    student_class =models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-updated', ]
        
        
    def __str__(self):
        return self.student_name

    
class Post (models.Model):
    title = models.CharField(max_length=255)
    school_post = models.ForeignKey(School, on_delete=models.CASCADE)
    body = models.TextField(help_text='Enter post here...')
    deptors_list = models.ForeignKey(Debtor, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_pics', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    
    class Meta:
        ordering = ['-updated', ]
    
    def __str__(self):
        return self.title

class Comment (models.Model):
    school = models.ForeignKey(School, on_delete = models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(help_text='Enter your comments here...')
    created = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        ordering = ['-created', ]
    def __str__(self):
        return self.body
    
class Reply (models.Model):
    school = models.ForeignKey(School, on_delete = models.CASCADE, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    body = models.TextField(help_text='Enter your comments here...')
    created = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        ordering = ['-created', ]
    def __str__(self):
        return self.body


class Contend (models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    student_id = models.CharField(max_length=50)
    how_to_be_contacted = models.CharField(max_length=255, help_text='specify email or phone number')
    complain = models.TextField(help_text='Enter your complain here...')

    def __str__(self):
        return self.student_id

class Help (models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title
    
    
class Message(models.Model):
    Full_name = models.CharField(max_length=255)
    Email_address = models.EmailField(max_length=255)
    Subject = models.CharField(max_length=255)
    message = models.TextField()


class Meeting(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    meeting_host = models.OneToOneField(School, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    participants = models.ManyToManyField(School, related_name='Main', blank=True)
    meeting_profile_image = models.ImageField(upload_to='Meeting DP', default='fixed.jpg')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created', ]
        
    def __str__(self):
        return self.title
    

class Meeting_Comment(models.Model):
    body = models.TextField()
    image = models.ImageField(upload_to='MettingCommentImage', null=True, blank= True)
    attendee = models.ForeignKey(School, on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created', ]
        
    def __str__(self):
        return self.body
    
    
class Meeting_Comment_Reply(models.Model):
    body = models.TextField()
    image = models.ImageField(upload_to='Metting_Comment_Reply_image', null=True, blank= True)
    responder = models.ForeignKey(School, on_delete=models.CASCADE)
    comment = models.ForeignKey(Meeting_Comment, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created', ]
        
    def __str__(self):
        return self.body
    
   
class School_Chat(models.Model):
    sender = models.ForeignKey(School, on_delete=models.CASCADE) 
    recepient = models.ForeignKey(School, on_delete=models.CASCADE, related_name='receiver') 
    body = models.TextField()
    image = models.ImageField(upload_to='Chat_image', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created', ]
    
    
    def __str__(self):
        return f' {self.sender} Chat '