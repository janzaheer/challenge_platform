# Generated by Django 2.0.13 on 2020-05-11 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20200508_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberchatroom',
            name='status',
            field=models.CharField(blank=True, choices=[('requested', 'requested'), ('approved', 'approved'), ('cancle', 'cancle')], default='cancle', max_length=200, null=True),
        ),
    ]
