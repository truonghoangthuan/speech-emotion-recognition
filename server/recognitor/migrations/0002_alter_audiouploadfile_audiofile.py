# Generated by Django 4.1.3 on 2022-12-01 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recognitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiouploadfile',
            name='audioFile',
            field=models.FileField(upload_to='audio_files/'),
        ),
    ]
