# Generated by Django 4.0.4 on 2022-04-19 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knox', '0009_authtoken_ip_authtoken_user_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='authtoken',
            name='last_activity',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
