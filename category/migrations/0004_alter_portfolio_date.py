# Generated by Django 4.0 on 2022-03-20 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_alter_portfolio_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]