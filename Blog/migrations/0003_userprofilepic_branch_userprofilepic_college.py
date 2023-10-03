# Generated by Django 4.2.5 on 2023-10-01 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Blog", "0002_alter_comments_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofilepic",
            name="branch",
            field=models.CharField(
                blank=True,
                choices=[
                    ("CSE", "Computer Science and Engineering"),
                    ("CSE_DS", "Computer Science and Engineering (Data Science)"),
                    ("CSE_CS", "Computer Science and Engineering (Cyber Security)"),
                    ("ISE", "Information Science and Engineering"),
                    ("EE", "Electrical Engineering"),
                    ("ME", "Mechanical Engineering"),
                    ("TE", "Telecommunication Engineering"),
                    ("IEM", "Industrial Engineering and Management"),
                    ("AIML", "Artificial Intelligence and Machine Learning"),
                    ("AE", "Aerospace Engineering"),
                    ("MCA", "Masters of Computer Applications"),
                    ("ECE", "Electronics and Telecommunication Engineering"),
                    ("EIE", "Electrinics and Instrumentation Engineering"),
                    ("EEE", "Electrical and Electrinics Engineering"),
                    ("CE", "Chemical Engineering"),
                    ("CV", "Civil Engineering"),
                    ("BT", "Biotechnology"),
                ],
                default="",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="userprofilepic",
            name="college",
            field=models.CharField(
                blank=True,
                choices=[
                    ("RVCE", "R.V. College of Engineering"),
                    ("RVU", "R.V. University"),
                ],
                default="",
                max_length=30,
                null=True,
            ),
        ),
    ]
