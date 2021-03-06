# Generated by Django 3.2.3 on 2021-05-19 16:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('About_me', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Clinic_timing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sunday', models.CharField(max_length=25)),
                ('Monday', models.CharField(max_length=25)),
                ('Tuesday', models.CharField(max_length=25)),
                ('Wednesday', models.CharField(max_length=25)),
                ('Thursday', models.CharField(max_length=25)),
                ('Friday', models.CharField(max_length=25)),
                ('Saturday', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Contact_me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contact_me_info', models.TextField(blank=True)),
                ('Address', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=14)),
                ('Email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('My_skills', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Latest_news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/images')),
                ('News_title', models.CharField(max_length=60)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('Short_news', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='My_skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('My_skills', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Other_professional_skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('My_skills', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personal_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(max_length=40)),
                ('Address', models.CharField(max_length=100)),
                ('Qualification', models.CharField(max_length=100)),
                ('NMC_Number', models.CharField(max_length=40)),
                ('Speciality', models.CharField(max_length=200)),
                ('Phone', models.CharField(max_length=14)),
                ('Email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('Website', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Socail_media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Facebook', models.CharField(max_length=50)),
                ('Twitter', models.CharField(max_length=50)),
                ('Instagram', models.CharField(max_length=50)),
                ('LinkedIn', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Training_and_advance_skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('My_skills', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Training_and_advance_skill_slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/images')),
                ('Title', models.CharField(max_length=40)),
                ('Short_description', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Work_experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Work_experience_field', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Work_experience_location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Work_experience_location', models.CharField(max_length=80)),
                ('Work_experience_period', models.CharField(max_length=20)),
                ('Work_experience_short_title', models.CharField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
