# Generated by Django 5.1.1 on 2024-10-01 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_portfolio_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='project_desc',
            field=models.CharField(max_length=500),
        ),
    ]
