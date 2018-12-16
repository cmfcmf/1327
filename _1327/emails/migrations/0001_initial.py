# Generated by Django 2.0.9 on 2018-12-06 20:29

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_name', models.CharField(max_length=255)),
                ('from_address', models.CharField(max_length=255)),
                ('to_names', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
                ('to_addresses', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
                ('cc_names', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
                ('cc_addresses', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
                ('subject', models.CharField(max_length=512)),
                ('date', models.DateTimeField()),
                ('text', models.TextField()),
                ('num_attachments', models.IntegerField(default=0)),
                ('message_id', models.CharField(max_length=512)),
                ('in_reply_to', models.CharField(max_length=512, null=True)),
                ('references', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=512), size=None)),
                ('envelope', models.FileField(upload_to='')),
                ('trello_card_id', models.CharField(max_length=255, null=True)),
                ('archived', models.BooleanField(default=False)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='emails.Email')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]