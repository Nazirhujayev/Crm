# Generated by Django 5.1.2 on 2024-12-25 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='brith',
            new_name='birth',
        ),
    ]
