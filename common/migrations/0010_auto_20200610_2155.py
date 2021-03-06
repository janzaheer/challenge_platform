# Generated by Django 2.0.13 on 2020-06-10 21:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0009_auto_20200604_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberchatroom',
            name='status',
            field=models.CharField(blank=True, choices=[('requested', 'requested'), ('approved', 'approved'), ('cancel', 'cancel')], default='cancel', max_length=200, null=True),
        ),
        migrations.RemoveField(
            model_name='memberchatroom',
            name='user',
        ),
        migrations.AddField(
            model_name='memberchatroom',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='user_member_chat_room', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
