# Generated by Django 4.1.6 on 2023-02-09 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapi', '0002_alter_crud_email_alter_crud_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crud',
            name='email',
            field=models.TextField(max_length=40),
        ),
    ]