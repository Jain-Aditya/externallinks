# Generated by Django 2.2 on 2019-06-28 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0005_auto_20190628_1221'),
        ('links', '0005_linkevent_user_is_bot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkevent',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='organisations.User'),
        ),
    ]
