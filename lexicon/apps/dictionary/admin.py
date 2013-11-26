# -*- encoding: utf-8 -*-
"""Defines all models to admin for Django Admin UI."""
from django.contrib import admin
from models import *

admin.site.register(Skill)
admin.site.register(SLC)
admin.site.register(FLC)
admin.site.register(Category)
admin.site.register(Word)
admin.site.register(SLCHasSkill)
admin.site.register(FLCHasSLC)
admin.site.register(CategoryHasFLC)
admin.site.register(WordHasSkill)