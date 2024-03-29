# Generated by Django 4.0.4 on 2022-05-20 22:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('assignmentid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AssignmentGeneral',
            fields=[
                ('assid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=300)),
                ('duedate', models.DateField()),
                ('duetime', models.TimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('admin', 'Admin'), ('instructor', 'Instructor'), ('student', 'Student')], max_length=50)),
                ('userid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('reviewid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='reviewFiles/')),
                ('body', models.TextField(max_length=3000)),
                ('assignmentid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='review.assignment')),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('uploadid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('body', models.TextField(max_length=3000)),
                ('file', models.FileField(blank=True, null=True, upload_to='uploadFiles/')),
                ('assignmentid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='review.assignment')),
                ('reviewid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='review.review')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('courseid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='review.course')),
                ('studentid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='review.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Reviewer',
            fields=[
                ('reviewid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('assgeneral', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='review.assignmentgeneral')),
                ('assigneeid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='review.assignment')),
                ('reviewer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='review.profile')),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='reviewerid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='review.reviewer'),
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='review.profile'),
        ),
        migrations.AddField(
            model_name='assignmentgeneral',
            name='courseid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='review.course'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='assgeneral',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='review.assignmentgeneral'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='assignee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='review.profile'),
        ),
    ]
