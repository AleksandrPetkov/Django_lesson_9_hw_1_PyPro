# Generated by Django 4.1.5 on 2023-01-19 09:42

from django.db import migrations, models
import students.validators


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_age_student_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, validators=[students.validators.validate_unique_email]),
        ),
    ]
