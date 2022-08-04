from django.db import models
from django.utils import timezone
from shortuuid.django_fields import ShortUUIDField

class Locality (models.Model):
    country = models.CharField(max_length=100)
    ctate = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    local_government = models.CharField(max_length=100)
    
    def __str__(self):
        return self.local_government

class School (models.Model):
    school_owner = models.CharField(max_length=255)
    school_name = models.CharField(max_length=255)
    school_id = ShortUUIDField(
        length= 5,
        max_length = 7,
        prefix = 'DebPay',
        alphabet = "123456efghij",
        primary_key = True
    )
    reg_number = models.CharField(max_length=255)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE)
    debtor = models.ManyToManyField('Debtor', blank=True)
    email = models.EmailField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.school_name


class School_Profile (models.Model):
    school = models.OneToOneField(School, on_delete=models.CASCADE)
    profile_pics = models.ImageField(default='default.png',  upload_to='profile_pics')

    def __str__(self):
        return self.school

class Debtor (models.Model):
    student_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100)
    sponsor_email = models.EmailField(max_length=100, unique=True)
    sponsor_No = models.CharField(max_length=15, default=+234)
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

class Debtors_profile (models.Model):
    debtor = models.ForeignKey(Debtor, on_delete=models.CASCADE)
    profile_pics = models.ImageField(default='default.png',  upload_to='debt_profile_pics')

    def __str__(self):
        return self.debtor

class Post (models.Model):
    title = models.CharField(max_length=255)
    school_post = models.ForeignKey(School, on_delete=models.CASCADE)
    body = models.TextField(help_text='Enter post here...')
    deptors_list = models.ForeignKey(Debtors_profile, on_delete=models.CASCADE)
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

    def __str__(self)
        return self.title
