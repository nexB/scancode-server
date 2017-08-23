# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-23 07:54
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Copyright',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_line', models.IntegerField(help_text='Start line of the copyright')),
                ('end_line', models.IntegerField(help_text='End line of the copyright')),
            ],
        ),
        migrations.CreateModel(
            name='CopyrightAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(help_text='Copyright author of the copyright', max_length=200)),
                ('copyright', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scanapp.Copyright')),
            ],
        ),
        migrations.CreateModel(
            name='CopyrightHolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holder', models.CharField(help_text='Copyright holder of the copyright', max_length=400)),
                ('copyright', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scanapp.Copyright')),
            ],
        ),
        migrations.CreateModel(
            name='CopyrightStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.CharField(help_text='Copyright statement of the copyright', max_length=500)),
                ('copyright', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scanapp.Copyright')),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(help_text='Key of license', max_length=200)),
                ('score', models.IntegerField(help_text='Score of license')),
                ('short_name', models.CharField(help_text='Short name of the license', max_length=200)),
                ('category', models.CharField(help_text='Category of license', max_length=1000)),
                ('owner', models.CharField(help_text='Owner of the license', max_length=500)),
                ('homepage_url', models.URLField(help_text='Homepage url of license', max_length=2000)),
                ('text_url', models.URLField(help_text='Text url of license', max_length=2000)),
                ('dejacode_url', models.URLField(help_text='Dejacode url of detected license', max_length=2000)),
                ('spdx_license_key', models.CharField(help_text='Spdx license key', max_length=200)),
                ('spdx_url', models.URLField(help_text='Spdx url of license', max_length=2000)),
                ('start_line', models.IntegerField(help_text='Start line of license')),
                ('end_line', models.IntegerField(help_text='End line of license in the file')),
                ('matched_rule', django.contrib.postgres.fields.jsonb.JSONField(help_text='Matched rule about the license detected')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', django.contrib.postgres.fields.jsonb.JSONField(help_text='Information of the package', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Scan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, help_text='Url from where the code is fetched', max_length=2000, null=True)),
                ('scan_directory', models.CharField(blank=True, help_text='Directory in which the code to be scanned is stored', max_length=2000, null=True)),
                ('scancode_notice', models.CharField(blank=True, help_text='Notice by the scancode-toolkit', max_length=2000, null=True)),
                ('scancode_version', models.CharField(blank=True, help_text='Version of scancode being used', max_length=200, null=True)),
                ('files_count', models.IntegerField(blank=True, default=0, help_text='Number of files under scan', null=True)),
                ('scan_start_time', models.DateTimeField(blank=True, help_text='Time at which scan starts', null=True)),
                ('scan_end_time', models.DateTimeField(blank=True, help_text='Time at which scan ends', null=True)),
                ('user', models.ForeignKey(blank=True, help_text='Logged in user', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ScanError',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scan_error', models.CharField(help_text='Information about the scan errors', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ScannedFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(help_text='Path of file scanned', max_length=400)),
                ('type', models.CharField(help_text='Type of the entity being scanned', max_length=400)),
                ('name', models.CharField(help_text='Name of the entity being scanned', max_length=400)),
                ('base_name', models.CharField(help_text='Base name of entity without extension', max_length=400)),
                ('extension', models.CharField(blank=True, help_text='Extension of the entity being scanned', max_length=400, null=True)),
                ('date', models.DateTimeField(blank=True, help_text='Date of entity being created', null=True)),
                ('size', models.IntegerField(help_text='Size of the entity being scanned')),
                ('sha1', models.CharField(blank=True, help_text='SHA1 Checksums of the file', max_length=400, null=True)),
                ('md5', models.CharField(blank=True, help_text='MD5 checksums of the file', max_length=400, null=True)),
                ('files_count', models.IntegerField(blank=True, help_text='number of files present if a directory', null=True)),
                ('mime_type', models.CharField(blank=True, help_text='mime type of entity being scanned', max_length=400, null=True)),
                ('file_type', models.CharField(blank=True, help_text='file type of entity being scanned. null if the entity is a directory', max_length=400, null=True)),
                ('programming_language', models.CharField(blank=True, help_text='programming language used in the entity', max_length=400, null=True)),
                ('is_binary', models.BooleanField(help_text='Whether the entity being scanned is binary or not')),
                ('is_text', models.BooleanField(help_text='Whether the entity being scanned has text or not')),
                ('is_archive', models.BooleanField(help_text='Whether the entity being scanned is archive or not')),
                ('is_media', models.BooleanField(help_text='Whether the entity being scanned is media file or not')),
                ('is_source', models.BooleanField(help_text='Whether the entity being scanned is source or not')),
                ('is_script', models.BooleanField(help_text='Whether the entity being scanned is a script file or not')),
                ('scan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scanapp.Scan')),
            ],
        ),
        migrations.AddField(
            model_name='scanerror',
            name='scanned_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scanapp.ScannedFile'),
        ),
        migrations.AddField(
            model_name='package',
            name='scanned_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scanapp.ScannedFile'),
        ),
        migrations.AddField(
            model_name='license',
            name='scanned_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scanapp.ScannedFile'),
        ),
        migrations.AddField(
            model_name='copyright',
            name='scanned_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scanapp.ScannedFile'),
        ),
    ]
