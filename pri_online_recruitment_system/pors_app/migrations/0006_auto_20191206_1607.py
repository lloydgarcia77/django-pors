# Generated by Django 2.2.3 on 2019-12-06 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pors_app', '0005_auto_20191206_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priapplicantexamscoret1peinfo',
            name='applicant_exam_score_t1pe',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='applicant_exam_score_t1pe_fk', to='pors_app.PRIApplicantProfileInfo'),
        ),
    ]