# Generated by Django 4.0 on 2022-04-09 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0005_rename_workdate_educationcard_eddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationcard',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='educationcard',
            name='title',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='workexperiencecard',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='workexperiencecard',
            name='title',
            field=models.CharField(max_length=70),
        ),
    ]