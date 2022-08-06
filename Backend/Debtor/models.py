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
    School_owner = models.CharField(max_length=255)
    School_name = models.CharField(max_length=255)
    school_id = ShortUUIDField(
        length= 4,
        max_length = 10,
        prefix = 'DP',
        alphabet = "123456efghij",
        primary_key = True
    )
    Reg_number = models.CharField(max_length=255)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['username']
    
    
  
    def __str__(self):
        return self.School_name


class School_Profile (models.Model):
    school = models.OneToOneField(School, on_delete=models.CASCADE)
    profile_pics = models.ImageField(default='fixed.png', upload_to='profile_pics')
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE,  blank=True, null=True)
    debtor = models.ManyToManyField('Debtor', blank=True)

    def __str__(self):
        return f'{self.school.School_name} Profile'

class Debtor (models.Model):
    student_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100)
    sponsor_email = models.EmailField(max_length=100, unique=True)
    sponsor_relationship = models.CharField(max_length=50)
    sponsor_name = models.CharField(max_length=255)
    sponsor_location = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    debt = models.CharField(max_length=50)
    student_class =models.ForeignKey('Level', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_id

class Level (models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.name
    

class Deptors_profile (models.Model):
    debtor = models.ForeignKey(Debtor, on_delete=models.CASCADE)
    profile_pics = models.ImageField(default='fixed.jpg', upload_to='debt_profile_pics')

    def __str__(self):
        return f'{self.debtor.Student_name} Profile'
    
class Post (models.Model):
    title = models.CharField(max_length=255)
    school_post = models.ForeignKey(School, on_delete=models.CASCADE)
    body = models.TextField(help_text='Enter post here...')
    deptors_list = models.ForeignKey(Deptors_profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_pics', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment (models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(help_text='Enter your comments here...')
    created = models.DateTimeField(auto_now_add=True)

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
    body = models.TextField(help_text='Enter help here')

    def __str__(self):
        return self.title
    
    
class Message(models.Model):
    Full_name = models.CharField(max_length=255)
    Email_address = models.EmailField(max_length=255)
    Subject = models.CharField(max_length=255)
    message = models.TextField()
