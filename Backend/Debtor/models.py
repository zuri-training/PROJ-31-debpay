from django.db import models
from django.utils import timezone
from shortuuid.django_fields import ShortUUIDField


class Locality (models.Model):
    Country = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Local_Government = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Local_Government

class School (models.Model):
    School_owner = models.CharField(max_length=255)
    School_name = models.CharField(max_length=255)
    school_id = ShortUUIDField(
        length= 5,
        max_length = 7,
        prefix = 'DebPay',
        alphabet = "123456efghij",
        primary_key = True
    )
    Reg_number = models.CharField(max_length=255)
    Locality = models.ForeignKey(Locality, on_delete=models.CASCADE)
    debtor = models.ManyToManyField('Debtor', blank=True)
    Email = models.EmailField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.School_name


class School_Profile (models.Model):
    school = models.OneToOneField(School, on_delete=models.CASCADE)
    profile_pics = models.ImageField(default='default.png',  upload_to='profile_pics')

    def __str__(self):
        return self.school

class Debtor (models.Model):
    Student_name = models.CharField(max_length=100)
    Student_id = models.CharField(max_length=100)
    Sponsor_email = models.EmailField(max_length=100, unique=True)
    Sponsor_No = models.CharField(max_length=15, default=+234)
    Sponsor_location = models.CharField(max_length=255)
    Full_name = models.CharField(max_length=255)
    Debt = models.CharField(max_length=50)
    Student_class =models.ForeignKey('Level', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Student_id

class Level (models.Model):
    Name = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.Name

class Deptors_profile (models.Model):
    debtor = models.ForeignKey(Debtor, on_delete=models.CASCADE)
    profile_pics = models.ImageField(default='default.png',  upload_to='debt_profile_pics')

    def __str__(self):
        return self.debtor

class Post (models.Model):
    Title = models.CharField(max_length=255)
    school_post = models.ForeignKey(School, on_delete=models.CASCADE)
    Body = models.TextField(help_text='Enter post here...')
    deptors_list = models.ForeignKey(Debtor, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_pics', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title

class Comment (models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    Body = models.TextField(help_text='Enter your comments here...')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Body


class Contend (models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    Email = models.EmailField(max_length=100)
    Student_id = models.CharField(max_length=50)
    How_to_be_contacted = models.CharField(max_length=255, help_text='specify email or phone number')
    Complain = models.TextField(help_text='Enter your complain here...')

    def __str__(self):
        return self.Student_id

class Help (models.Model):
    Title = models.CharField(max_length=255)
    Body = models.TextField(help_text='Enter help here')

    def __str__(self):
        return self.Title