# Generated by Django 4.0.4 on 2022-05-28 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0013_course_picture_alter_reviewer_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmentgeneral',
            name='picture',
            field=models.ImageField(blank=True, default='/pictures/assignment.png', null=True, upload_to='pictures/'),
        ),
    ]
