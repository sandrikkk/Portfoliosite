# Generated by Django 4.0 on 2022-04-03 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0004_alter_codingskills_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='educationcard',
            old_name='workdate',
            new_name='eddate',
        ),
    ]
