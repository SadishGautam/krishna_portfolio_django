from django.contrib import admin
from .models import Greeting, About_me,Personal_details,My_skills,Other_professional_skills,Education,Training_and_advance_skill,Training_and_advance_skill_slider,Work_experience,Work_experience_location,Latest_news,Contact_me,Clinic_timing,Social_media

# Register your models here.


admin.site.register(Greeting)
admin.site.register(About_me)
admin.site.register(Personal_details)
admin.site.register(My_skills)
admin.site.register(Other_professional_skills)
admin.site.register(Education)
admin.site.register(Training_and_advance_skill)
admin.site.register(Training_and_advance_skill_slider)
admin.site.register(Work_experience)
admin.site.register(Work_experience_location)
admin.site.register(Latest_news)
admin.site.register(Contact_me)
admin.site.register(Clinic_timing)
admin.site.register(Social_media)