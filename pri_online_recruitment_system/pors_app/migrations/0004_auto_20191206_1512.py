# Generated by Django 2.2.3 on 2019-12-06 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pors_app', '0003_auto_20191206_1459'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PRIApplicantExamScoreARP',
            new_name='PRIApplicantExamScoreARPInfo',
        ),
        migrations.RenameModel(
            old_name='PRIApplicantExamScoreCCA',
            new_name='PRIApplicantExamScoreCCAInfo',
        ),
        migrations.RenameModel(
            old_name='PRIApplicantExamScoreSCCT',
            new_name='PRIApplicantExamScoreSCCTInfo',
        ),
        migrations.RenameModel(
            old_name='PRIApplicantExamScoreT1PE',
            new_name='PRIApplicantExamScoreT1PEInfo',
        ),
        migrations.RenameModel(
            old_name='PRIApplicantExamScoreT2SE',
            new_name='PRIApplicantExamScoreT2SEInfo',
        ),
        migrations.RenameModel(
            old_name='PRIApplicantExamScoreT3E',
            new_name='PRIApplicantExamScoreT3EInfo',
        ),
        migrations.RenameModel(
            old_name='PRIApplicantExamScoreT3PTSCT',
            new_name='PRIApplicantExamScoreT3PTSCTInfo',
        ),
        migrations.RenameModel(
            old_name='PRIApplicantExamScoreT4AR',
            new_name='PRIApplicantExamScoreT4ARInfo',
        ),
    ]
