# Generated by Django 2.2 on 2019-04-04 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutodeskAPIs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]