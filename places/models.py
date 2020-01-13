# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Place(models.Model):
    place_id = models.CharField(primary_key=True, max_length=200, unique=True, db_index=True)
    name = models.CharField(max_length=200, db_index=True)
