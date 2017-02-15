# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 17:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import topnotchdev.files_widget.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileIcon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extension', models.CharField(blank=True, max_length=100, null=True)),
                ('image', topnotchdev.files_widget.fields.ImageField(max_length=200)),
                ('display_text_overlay', models.BooleanField(default=True)),
                ('overlay_text', models.CharField(blank=True, help_text=b'Leave blank to display file extension', max_length=7, null=True)),
                ('base_color', models.CharField(blank=True, max_length=12, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IconSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('css_path', models.CharField(blank=True, help_text=b'Optional css file for icon styling', max_length=200, null=True)),
                ('active', models.BooleanField(default=True)),
                ('priority', models.IntegerField(default=1)),
                ('default_icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='files_widget.FileIcon')),
            ],
        ),
        migrations.CreateModel(
            name='GlobalPermission',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('auth.permission',),
        ),
        migrations.AddField(
            model_name='fileicon',
            name='icon_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='files_widget.IconSet'),
        ),
    ]
