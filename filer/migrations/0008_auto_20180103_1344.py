# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file_ptr',
            field=models.OneToOneField(serialize=False, related_name='filer_image_file', parent_link=True, to='filer.File', primary_key=True),
        ),
        migrations.AlterField(
            model_name='folderpermission',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.deletion.SET_NULL, related_name='filer_folder_permissions', to='auth.Group', verbose_name='group'),
        ),
    ]
