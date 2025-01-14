# Generated by Django 4.0.4 on 2022-04-18 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knox', '0008_remove_authtoken_salt'),
    ]

    operations = [
        migrations.AddField(
            model_name='authtoken',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True, verbose_name='IP'),
        ),
        migrations.AddField(
            model_name='authtoken',
            name='user_agent',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
