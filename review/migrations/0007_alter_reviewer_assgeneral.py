# Generated by Django 4.0.4 on 2022-05-26 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0006_alter_reviewer_assgeneral'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewer',
            name='assgeneral',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='review.assignmentgeneral'),
        ),
    ]