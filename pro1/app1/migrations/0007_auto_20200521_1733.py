# Generated by Django 3.0.3 on 2020-05-21 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20200521_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_detail',
            name='Name',
            field=models.TextField(),
        ),
    ]