# Generated by Django 4.1.5 on 2023-01-21 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("report", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="status",
            field=models.IntegerField(
                choices=[
                    (0, "No Response"),
                    (1, "Viewed"),
                    (2, "Contacted"),
                    (3, "Interviewed"),
                    (4, "Accepted"),
                    (5, "Rejected"),
                ]
            ),
        ),
    ]
