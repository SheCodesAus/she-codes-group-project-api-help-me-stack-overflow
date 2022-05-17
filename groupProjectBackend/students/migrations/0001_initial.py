# Generated by Django 4.0.2 on 2022-05-17 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('modefied_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='students.basemodel')),
                ('name', models.CharField(max_length=200)),
                ('contact_email', models.CharField(max_length=200)),
                ('contact_phone', models.CharField(max_length=200)),
                ('biography', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('demographic_gender', models.CharField(max_length=200)),
                ('demographic_nationality', models.CharField(max_length=200)),
                ('social_linkedin', models.URLField()),
                ('social_github', models.URLField()),
                ('employment_company', models.CharField(max_length=200)),
                ('employment_position', models.CharField(max_length=200)),
                ('employment_industry', models.CharField(max_length=200)),
                ('employment_salary', models.IntegerField()),
                ('program_attendence', models.CharField(max_length=200)),
                ('coding_languages', models.CharField(max_length=200)),
            ],
            bases=('students.basemodel',),
        ),
    ]