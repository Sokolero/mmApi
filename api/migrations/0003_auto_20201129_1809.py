# Generated by Django 3.1.3 on 2020-11-29 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201111_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='user',
        ),
        migrations.AlterField(
            model_name='gallery',
            name='object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallerys', to='api.object'),
        ),
    ]
