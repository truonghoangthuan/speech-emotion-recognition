# Generated by Django 4.1.3 on 2022-12-01 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioUploadFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audioFile', models.FileField(upload_to='audioFiles/')),
                ('textOutput', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]