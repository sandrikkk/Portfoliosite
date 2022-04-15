# Generated by Django 4.0 on 2022-03-13 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workdate', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperienceCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workdate', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
    ]