# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 03:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('from_player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hudunit.Player')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='from_player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hudunit.Player'),
        ),
        migrations.AddField(
            model_name='answer',
            name='to_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hudunit.Question'),
        ),
    ]
