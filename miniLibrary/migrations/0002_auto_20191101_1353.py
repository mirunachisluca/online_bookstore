# Generated by Django 2.2.6 on 2019-11-01 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miniLibrary', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='order',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
