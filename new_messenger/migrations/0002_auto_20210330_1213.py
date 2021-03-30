# Generated by Django 3.1.7 on 2021-03-30 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_messenger', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='image',
            field=models.ImageField(upload_to='chats/<django.db.models.fields.CharField>_<django.db.models.fields.related.ForeignKey>/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='chatuser',
            name='image',
            field=models.ImageField(upload_to='users/<django.db.models.fields.CharField>/', verbose_name='Фото'),
        ),
    ]