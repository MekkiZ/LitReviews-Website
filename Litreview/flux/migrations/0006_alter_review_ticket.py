# Generated by Django 4.1.2 on 2022-10-21 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flux', '0005_userfollows_followed_user_userfollows_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='ticket',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='flux.ticket'),
            preserve_default=False,
        ),
    ]
