import profile
from tkinter import CASCADE
from unicodedata import name
from django.db import models
from django.forms import PasswordInput

#model for schools this is to create instance into the database
class School (models.Model):
    School_owner = models.CharField(max_length=255)
    School_name = models.CharField(max_length=255)
    Reg_number = models.CharField(max_length=255)
    Locality = models.CharField( max_length=255)
    Debtor = models.CharField(max_length=255, primary_key=True, blank=False)
    Email = models.CharField(max_length=255, help_text='Enter valid email')
    Password = models.CharField( max_length=20, help_text='Enter valid password')
        
    # this method allow us to return str rather than object
    # in the database we will have  school name
    def __str__(self):
        return self.School_name


#model for school profile
class School_Profile (models.Model):
    School = models.ForeignKey(School, on_delete=models.CASCADE)
    profile_pics = models.ImageField()

    #function to return school instead of obj
    def __str__(self):
        return self.School


#model for locality 
class Locality (models.Model):
    Country = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Local_Government = models.CharField(max_length=50)

    #return local government 
    def __str__(self):
        return self.Local_Government


#model for debtor
class Debtor (models.Model):
    Student_id = models.CharField(max_length=12, unique=True, primary_key=True)
    Sponsor_email = models.CharField(max_length=50)
    Sponsor_No = models.CharField(max_length=15, default=+234, editable= True)
    Sponsor_location = models.CharField(max_length=255)
    Full_name = models.CharField(max_length=255)
    Debt = models.CharField(max_length=50)
    Student_class =models.CharField(max_length=20)

    #return student ID as the str method
    def __str__(self):
        return self.Student_id


#model for level
class Level (models.Model):
    Name = models.CharField(max_length=50, blank=True, null=True)


#model for debtor's profile
class Deptors_profile (models.Model):
    Deptor = models.ForeignKey(Debtor, on_delete=models.CASCADE)
    Profile_pics = models.ImageField()

    #return deptor 
    def __str__(self):
        return self.Deptor


#model for post by schools
class Post (models.Model):
    Title = models.CharField(max_length=255)
    School = models.ForeignKey(School, on_delete=models.CASCADE)
    Body = models.TextField(help_text='Enter post here...')
    # I dont get this desptors field
    Deptors = models.CharField(max_length=255)
    image = models.ImageField()
    Date = models.DateTimeField(auto_created=True)

    #return title or school --------------later discuss
    def __str__(self):
        return self.Title, #self.School


#model for comments
class Comment (models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    Body = models.TextField(help_text='Enter your comments here...')
    Date = models.DateTimeField(auto_created=True)

    #return body
    def __str__(self):
        return self.Body


#model for contend
class Contend (models.Model):
    School = models.ForeignKey(School, on_delete=models.CASCADE)
    Email = models.CharField(max_length=50)
    Student_id = models.CharField(max_length=12, unique=True, primary_key=True)
    How_to_be_contacted = models.CharField(max_length=255, help_text='specify email or phone number')
    Complain = models.TextField(help_text='Enter your complain here...')

    #return student ID
    def __str__(self):
        return self.Student_id


#model for help
class Help (models.Model):
    Title = models.CharField(max_length=255)
    Body = models.TextField(help_text='Enter help here')

    #return title
    def __str__(self):
        return self.Title
