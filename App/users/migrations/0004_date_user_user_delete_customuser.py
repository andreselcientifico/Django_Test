# Generated by Django 4.2 on 2023-05-01 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_delete_date_user_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Names', models.CharField(max_length=20, verbose_name='Names')),
                ('Last_Names', models.CharField(max_length=20, verbose_name='Last Names')),
                ('Number_phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30, verbose_name='User Name')),
                ('anonymous_name', models.CharField(max_length=30, verbose_name='Anonymous Name')),
                ('password', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]