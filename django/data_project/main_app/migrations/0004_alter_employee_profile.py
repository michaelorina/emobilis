# Generated by Django 4.2.7 on 2023-11-08 09:20

from django.db import migrations, models
import main_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_employee_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile',
            field=models.ImageField(default='employees/employee_icon.png', null=True, upload_to=main_app.models.unique_img_name),
        ),
    ]
