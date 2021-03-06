# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-16 08:04
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models

import pretix.base.models.base
import pretix.plugins.badges.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pretixbase', '0088_auto_20180328_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='BadgeItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='badge_assignment', to='pretixbase.Item')),
            ],
        ),
        migrations.CreateModel(
            name='BadgeLayout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default', models.BooleanField(default=True, verbose_name='Default')),
                ('name', models.CharField(max_length=190, verbose_name='Name')),
                ('layout', models.TextField()),
                ('background', models.FileField(blank=True, max_length=255, null=True, upload_to=pretix.plugins.badges.models.bg_name)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='badge_layouts', to='pretixbase.Event')),
            ],
            options={
                'ordering': ('-default', 'name'),
            },
            bases=(models.Model, pretix.base.models.base.LoggingMixin),
        ),
        migrations.AddField(
            model_name='badgeitem',
            name='layout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='badges.BadgeLayout'),
        ),
    ]
