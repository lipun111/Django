# Generated by Django 2.2.5 on 2019-12-02 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('cemail', models.CharField(max_length=50)),
                ('caddrs', models.CharField(max_length=50)),
                ('cphone', models.CharField(max_length=50)),
                ('cincome', models.FloatField()),
            ],
        ),
    ]
