# Generated by Django 4.1.6 on 2023-02-20 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mongocrudApi', '0002_alter_mymongomodel_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymongomodel',
            name='cid',
            field=models.CharField(default='A1', max_length=100),
            preserve_default=False,
        ),
    ]
