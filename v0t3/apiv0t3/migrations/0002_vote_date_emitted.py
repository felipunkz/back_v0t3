# Generated by Django 2.2.1 on 2019-05-17 19:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('apiv0t3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='date_emitted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
