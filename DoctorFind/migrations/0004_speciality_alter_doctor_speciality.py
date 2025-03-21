# Generated by Django 4.1 on 2025-02-16 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("DoctorFind", "0003_alter_doctor_speciality"),
    ]

    operations = [
        migrations.CreateModel(
            name="Speciality",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name="doctor",
            name="speciality",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="DoctorFind.speciality"
            ),
        ),
    ]
