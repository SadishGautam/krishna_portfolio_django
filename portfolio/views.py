from django.shortcuts import render
from .models import Greeting, About_me,Personal_details,My_skills,Other_professional_skills,Education,Training_and_advance_skill,Training_and_advance_skill_slider,Work_experience,Work_experience_location,Latest_news,Contact_me,Clinic_timing,Social_media

# admin details 
# Name : Krishna-regmi
# Password : Regmi-11397
 

def index(request):
    greeting = Greeting.objects.get(id=1)             
    about_me= About_me.objects.get(id=1) 
    personal_details= Personal_details.objects.get(id=1) 
    my_skills= My_skills.objects.get(id=1) 
    other_professional_skills= Other_professional_skills.objects.get(id=1) 
    education= Education.objects.all()
    
    training_and_advance_skill= Training_and_advance_skill.objects.all()
    training_and_advance_skill_slider= Training_and_advance_skill_slider.objects.all()
    work_experience= Work_experience.objects.get(id=1) 
    work_experience_location= Work_experience_location.objects.all()
    latest_news= Latest_news.objects.all()
    contact_me= Contact_me.objects.get(id=1) 
    clinic_timing= Clinic_timing.objects.get(id=1)
    social_media= Social_media.objects.get(id=1)



    contex = {'greeting' : greeting,
            'about_me' : about_me,
            'personal_details' : personal_details,
            'my_skills' : my_skills,
            'other_professional_skills' : other_professional_skills,
            'education' : education,
            'training_and_advance_skill' : training_and_advance_skill,
            'training_and_advance_skill_slider' : training_and_advance_skill_slider,
            'work_experience' : work_experience,
            'work_experience_location' : work_experience_location,
            'latest_news' : latest_news,
            'contact_me' : contact_me,
            'clinic_timing' : clinic_timing,
            'social_media' : social_media,
            
              }


    return render(request, "index.html", contex)
