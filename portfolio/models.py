from django.db import models
from django.utils import timezone



class Greeting(models.Model):
    Greeting_title = models.CharField(max_length = 40,  default='Hello')
    Greeting_name = models.CharField(max_length = 40,  default='I AM DR. KRISHNA REGMI')
    Greeting_desc = models.CharField(max_length = 70,  default='& I am a Oral Maxillofacial Surgeon.')
    image = models.ImageField( upload_to='static/images', default='default.jpg')


    class Meta:
        verbose_name_plural = "Greeting"

    



class About_me(models.Model):
    About_me = models.TextField(blank = True)

    class Meta:
        verbose_name_plural = "About me (Update only)"


class Personal_details(models.Model):
    Full_name = models.CharField(max_length = 40)
    Address = models.CharField(max_length = 100)
    Qualification = models.CharField(max_length = 100)
    NMC_Number = models.CharField(max_length = 40)
    Speciality = models.CharField(max_length = 200)
    Phone = models.CharField(max_length = 14)
    Email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
    Website = models.CharField(max_length = 30)
    image = models.ImageField( upload_to='static/images', default='default.jpg')

    class Meta:
        verbose_name_plural = "Personal details (Update only)"



class My_skills(models.Model):
    My_skills = models.TextField(blank = True)

    class Meta:
        verbose_name_plural = "My skills (Update only)"



class Other_professional_skills(models.Model):
    My_skills = models.TextField(blank = True)
    
    class Meta:
        verbose_name_plural = "Other professional skills (Update only)"

class Education(models.Model):
    My_skills = models.CharField(max_length = 200)
    
    class Meta:
        verbose_name_plural = "Education"

class Training_and_advance_skill(models.Model):
    My_skills = models.TextField(blank = True)
    
    class Meta:
        verbose_name_plural = "Training_and_advance_skill (Update only)"

class Training_and_advance_skill_slider(models.Model):
    image = models.ImageField( upload_to='static/images', default='default.jpg')
    Title = models.CharField(max_length = 40)
    Short_description = models.CharField(max_length = 80)
    
    class Meta:
        verbose_name_plural = "Training and advance skill slider"



class Work_experience(models.Model):
    Work_experience_field = models.TextField(blank = True)
    
    class Meta:
        verbose_name_plural = "Work experience (Update only)"


class Work_experience_location(models.Model):
    Work_experience_hospital = models.CharField(max_length = 80)
    Work_experience_start_period = models.DateField((""), auto_now=False, auto_now_add=False, default="2018-03-14")
    Work_experience_end_period = models.CharField(max_length = 20)
    Work_experience_short_title = models.CharField(max_length = 40)
    
    class Meta:
        verbose_name_plural = "Work experience location"


class Latest_news(models.Model):
    image = models.ImageField( upload_to='static/images', default='default.jpg')
    News_title = models.CharField(max_length = 60)
    date = models.DateField(blank=True, null=True, default=timezone.now)
    Short_news = models.TextField(blank = True)
    
    class Meta:
        verbose_name_plural = "Latest news "


class Contact_me(models.Model):
    Contact_me_info = models.TextField(blank = True)
    Address = models.CharField(max_length = 100)
    Phone = models.CharField(max_length = 14)
    Email = models.EmailField(max_length=70,null=True, blank=True, unique=True)
    
    class Meta:
        verbose_name_plural = "Contact me (Update only)"



class Clinic_timing(models.Model):
    Sunday = models.CharField(max_length = 25)
    Monday = models.CharField(max_length = 25)
    Tuesday = models.CharField(max_length = 25)
    Wednesday = models.CharField(max_length = 25)
    Thursday = models.CharField(max_length = 25)
    Friday = models.CharField(max_length = 25)
    Saturday = models.CharField(max_length = 25)
    
    class Meta:
        verbose_name_plural = "Clinic timing (Update only)"



class Social_media(models.Model):
    Facebook = models.CharField(max_length = 50)
    Twitter = models.CharField(max_length = 50)
    Instagram = models.CharField(max_length = 50)
    LinkedIn = models.CharField(max_length = 50)
    
    class Meta:
        verbose_name_plural = "Social media (Update only)"



# admin details 
# Name : Krishna-regmi
# Password : Regmi-11397



    



