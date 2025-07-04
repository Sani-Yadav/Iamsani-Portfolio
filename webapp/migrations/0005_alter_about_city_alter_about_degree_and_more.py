# Generated by Django 5.2.1 on 2025-05-29 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0004_resume_delete_contactinfo_delete_portfolioitem_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="about",
            name="city",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="about",
            name="degree",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="about",
            name="email",
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name="about",
            name="freelance",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="about",
            name="heading",
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name="about",
            name="phone",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="about",
            name="website",
            field=models.CharField(max_length=50),
        ),
    ]
