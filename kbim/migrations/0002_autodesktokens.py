# Generated by Django 2.2 on 2019-04-05 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kbim', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutodeskTokens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=200)),
                ('refresh_token', models.CharField(max_length=200)),
                ('token_type', models.CharField(max_length=100)),
                ('expires_in', models.DateTimeField()),
            ],
        ),
    ]
