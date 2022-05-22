# Generated by Django 4.0.4 on 2022-05-22 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='group',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='reviewer',
            name='group',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='upload/reviewFiles/'),
        ),
        migrations.AlterField(
            model_name='upload',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='upload/uploadFiles/'),
        ),
    ]