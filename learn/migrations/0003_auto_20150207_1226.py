# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0002_article'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(default='tang', max_length=30),
            preserve_default=False,
        ),
    ]
