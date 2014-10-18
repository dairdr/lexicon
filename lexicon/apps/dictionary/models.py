# -*- encoding: utf-8 -*-
"""Defines all Dictionary's models.

Many of these modules are admin by Django Admin UI.

"""
from django.db import models

class Skill(models.Model):
	"""Skill table class."""
	name = models.CharField(max_length='45', db_column='name', null=False, blank=False)

	class Meta:
		db_table = 'dictionary_skill'
		ordering = ['id']

	def __unicode__(self):
		return '%s' % self.name

class SLC(models.Model):
	"""SLC table class."""
	name = models.CharField(max_length=45, db_column='name', null=False, blank=False)
	skill = models.ManyToManyField(Skill, through='SLCHasSkill')

	class Meta:
		db_table = 'dictionary_slc'
		ordering = ['id']

	def __unicode__(self):
		return '%s' % self.name

class SLCHasSkill(models.Model):
	"""SLCHasSkill table class."""
	slc = models.ForeignKey(SLC, db_column='slc', on_delete=models.PROTECT)
	skill = models.ForeignKey(Skill, db_column='skill', on_delete=models.PROTECT)

	class Meta:
		db_table = 'dictionary_slc_has_skill'

	def __unicode__(self):
		return 'relacion slc y skill (%s y %s)' % (self.slc.name, self.skill.name)

class FLC(models.Model):
	"""FLC table class."""
	name = models.CharField(max_length=45, db_column='name', null=False, blank=False)
	slc = models.ManyToManyField(SLC, through='FLCHasSLC')

	class Meta:
		db_table = 'dictionary_flc'
		ordering = ['id']

	def __unicode__(self):
		return '%s' % self.name

class FLCHasSLC(models.Model):
	"""FLCHasSLC table class."""
	flc = models.ForeignKey(FLC, db_column='flc', on_delete=models.PROTECT)
	slc = models.ForeignKey(SLC, db_column='slc', on_delete=models.PROTECT)

	class Meta:
		db_table = 'dictionary_flc_has_slc'

	def __unicode__(self):
		return 'relacion flc y slc (%s y %s)' % (self.flc.name, self.slc.name)

class Category(models.Model):
	"""Category table class."""
	name = models.CharField(max_length=45, db_column='name', null=False, blank=False)
	fcl = models.ManyToManyField(FLC, through='CategoryHasFLC')

	class Meta:
		db_table = 'dictionary_category'
		ordering = ['id']

	def __unicode__(self):
		return '%s' % self.name

class CategoryHasFLC(models.Model):
	"""CategoryHasFLC table class."""
	category = models.ForeignKey(Category, db_column='category', on_delete=models.PROTECT)
	flc = models.ForeignKey(FLC, db_column='flc', on_delete=models.PROTECT)

	class Meta:
		db_table = 'dictionary_category_has_flc'

	def __unicode__(self):
		return 'relacion entre category y flc (%s y %s)' % (self.category.name, self.flc.name)

class Word(models.Model):
	"""Word table class."""
	name = models.CharField(max_length=45, db_column='name')
	description = models.CharField(max_length=140, db_column='description', blank=True)
	image = models.ImageField(upload_to='dictionary/image', db_column='image', default='dictionary/image/default.png', null=False, blank=True)
	mark = models.CharField(max_length=45, db_column='mark', blank=True)
	map = models.CharField(max_length=45, db_column='map', blank=True)
	category = models.ForeignKey(Category, db_column='category', on_delete=models.PROTECT)
	order = models.PositiveIntegerField(db_column='order')
	skill = models.ManyToManyField(Skill, through='WordHasSkill')
	metaphor = models.ManyToManyField('Metaphor', null=True, blank=True)
	metonymy = models.ManyToManyField('Metonymy', null=True, blank=True)
	semantic_field = models.ManyToManyField('SemanticField', null=True, blank=True)

	class Meta:
		db_table = 'dictionary_word'
		ordering = ['order']

	def __unicode__(self):
		return '%s' % self.name

class WordHasSkill(models.Model):
	"""WordHasSkill table class."""
	word = models.ForeignKey(Word, db_column='word', on_delete=models.PROTECT)
	skill = models.ForeignKey(Skill, db_column='skill', on_delete=models.PROTECT)
	value = models.CharField(max_length=45, db_column='value', null=False, blank=False)

	class Meta:
		db_table = 'dictionary_word_has_skill'

	def __unicode__(self):
		return 'relacion word y flc (%s y %s)' % (self.word.name, self.skill.name)

class Metaphor(models.Model):
	"""Metaphor table class."""
	name = models.CharField(max_length=45, db_column='name')

	class Meta:
		db_table = 'dictionary_metaphor'
		ordering = ['name']

	def __unicode__(self):
		return self.name

class Metonymy(models.Model):
	"""Metonymy table class."""
	name = models.CharField(max_length=45, db_column='name')

	class Meta:
		db_table = 'dictionary_metonymy'
		ordering = ['name']

	def __unicode__(self):
		return self.name

class SemanticField(models.Model):
	"""SemanticField table class."""
	name = models.CharField(max_length=45, db_column='name')

	class Meta:
		db_table = 'dictionary_semantic_field'
		ordering = ['name']

	def __unicode__(self):
		return self.name