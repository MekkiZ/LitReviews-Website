# Generated by Django 4.1.2 on 2022-10-14 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flux', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='image'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='title',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
