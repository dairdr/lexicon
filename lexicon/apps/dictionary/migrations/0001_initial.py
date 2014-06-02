# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Skill'
        db.create_table('dictionary_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='45', db_column='name')),
        ))
        db.send_create_signal(u'dictionary', ['Skill'])

        # Adding model 'SLC'
        db.create_table('dictionary_slc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='name')),
        ))
        db.send_create_signal(u'dictionary', ['SLC'])

        # Adding model 'SLCHasSkill'
        db.create_table('dictionary_slc_has_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dictionary.SLC'], on_delete=models.PROTECT, db_column='slc')),
            ('skill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dictionary.Skill'], on_delete=models.PROTECT, db_column='skill')),
        ))
        db.send_create_signal(u'dictionary', ['SLCHasSkill'])

        # Adding model 'FLC'
        db.create_table('dictionary_flc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='name')),
        ))
        db.send_create_signal(u'dictionary', ['FLC'])

        # Adding model 'FLCHasSLC'
        db.create_table('dictionary_flc_has_slc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('flc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dictionary.FLC'], on_delete=models.PROTECT, db_column='flc')),
            ('slc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dictionary.SLC'], on_delete=models.PROTECT, db_column='slc')),
        ))
        db.send_create_signal(u'dictionary', ['FLCHasSLC'])

        # Adding model 'Category'
        db.create_table('dictionary_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='name')),
        ))
        db.send_create_signal(u'dictionary', ['Category'])

        # Adding model 'CategoryHasFLC'
        db.create_table('dictionary_category_has_flc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dictionary.Category'], on_delete=models.PROTECT, db_column='category')),
            ('flc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dictionary.FLC'], on_delete=models.PROTECT, db_column='flc')),
        ))
        db.send_create_signal(u'dictionary', ['CategoryHasFLC'])

        # Adding model 'Word'
        db.create_table('dictionary_word', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='name')),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=140, db_column='description', blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='dictionary/image/default.png', max_length=100, db_column='image', blank=True)),
            ('mark', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='mark', blank=True)),
            ('map', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='map', blank=True)),
            ('metaphor', self.gf('django.db.models.fields.files.ImageField')(default='dictionary/metaphor/default.png', max_length=100, db_column='metaphor', blank=True)),
            ('metonymy', self.gf('django.db.models.fields.files.ImageField')(default='dictionary/metonymy/default.png', max_length=100, db_column='metonymy', blank=True)),
            ('semantic_field', self.gf('django.db.models.fields.files.ImageField')(default='dictionary/semantic_field/default.png', max_length=100, db_column='semantic_field', blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dictionary.Category'], on_delete=models.PROTECT, db_column='category')),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(db_column='order')),
        ))
        db.send_create_signal(u'dictionary', ['Word'])

        # Adding model 'WordHasSkill'
        db.create_table('dictionary_word_has_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('word', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dictionary.Word'], on_delete=models.PROTECT, db_column='word')),
            ('skill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dictionary.Skill'], on_delete=models.PROTECT, db_column='skill')),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='value')),
        ))
        db.send_create_signal(u'dictionary', ['WordHasSkill'])


    def backwards(self, orm):
        # Deleting model 'Skill'
        db.delete_table('dictionary_skill')

        # Deleting model 'SLC'
        db.delete_table('dictionary_slc')

        # Deleting model 'SLCHasSkill'
        db.delete_table('dictionary_slc_has_skill')

        # Deleting model 'FLC'
        db.delete_table('dictionary_flc')

        # Deleting model 'FLCHasSLC'
        db.delete_table('dictionary_flc_has_slc')

        # Deleting model 'Category'
        db.delete_table('dictionary_category')

        # Deleting model 'CategoryHasFLC'
        db.delete_table('dictionary_category_has_flc')

        # Deleting model 'Word'
        db.delete_table('dictionary_word')

        # Deleting model 'WordHasSkill'
        db.delete_table('dictionary_word_has_skill')


    models = {
        u'dictionary.category': {
            'Meta': {'ordering': "['id']", 'object_name': 'Category'},
            'fcl': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['dictionary.FLC']", 'through': u"orm['dictionary.CategoryHasFLC']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'name'"})
        },
        u'dictionary.categoryhasflc': {
            'Meta': {'object_name': 'CategoryHasFLC', 'db_table': "'dictionary_category_has_flc'"},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dictionary.Category']", 'on_delete': 'models.PROTECT', 'db_column': "'category'"}),
            'flc': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dictionary.FLC']", 'on_delete': 'models.PROTECT', 'db_column': "'flc'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'dictionary.flc': {
            'Meta': {'ordering': "['id']", 'object_name': 'FLC'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'name'"}),
            'slc': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['dictionary.SLC']", 'through': u"orm['dictionary.FLCHasSLC']", 'symmetrical': 'False'})
        },
        u'dictionary.flchasslc': {
            'Meta': {'object_name': 'FLCHasSLC', 'db_table': "'dictionary_flc_has_slc'"},
            'flc': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dictionary.FLC']", 'on_delete': 'models.PROTECT', 'db_column': "'flc'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slc': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dictionary.SLC']", 'on_delete': 'models.PROTECT', 'db_column': "'slc'"})
        },
        u'dictionary.skill': {
            'Meta': {'ordering': "['id']", 'object_name': 'Skill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'45'", 'db_column': "'name'"})
        },
        u'dictionary.slc': {
            'Meta': {'ordering': "['id']", 'object_name': 'SLC'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'name'"}),
            'skill': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['dictionary.Skill']", 'through': u"orm['dictionary.SLCHasSkill']", 'symmetrical': 'False'})
        },
        u'dictionary.slchasskill': {
            'Meta': {'object_name': 'SLCHasSkill', 'db_table': "'dictionary_slc_has_skill'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dictionary.Skill']", 'on_delete': 'models.PROTECT', 'db_column': "'skill'"}),
            'slc': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dictionary.SLC']", 'on_delete': 'models.PROTECT', 'db_column': "'slc'"})
        },
        u'dictionary.word': {
            'Meta': {'ordering': "['order']", 'object_name': 'Word'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dictionary.Category']", 'on_delete': 'models.PROTECT', 'db_column': "'category'"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '140', 'db_column': "'description'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'dictionary/image/default.png'", 'max_length': '100', 'db_column': "'image'", 'blank': 'True'}),
            'map': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'map'", 'blank': 'True'}),
            'mark': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'mark'", 'blank': 'True'}),
            'metaphor': ('django.db.models.fields.files.ImageField', [], {'default': "'dictionary/metaphor/default.png'", 'max_length': '100', 'db_column': "'metaphor'", 'blank': 'True'}),
            'metonymy': ('django.db.models.fields.files.ImageField', [], {'default': "'dictionary/metonymy/default.png'", 'max_length': '100', 'db_column': "'metonymy'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'name'"}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'db_column': "'order'"}),
            'semantic_field': ('django.db.models.fields.files.ImageField', [], {'default': "'dictionary/semantic_field/default.png'", 'max_length': '100', 'db_column': "'semantic_field'", 'blank': 'True'}),
            'skill': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['dictionary.Skill']", 'through': u"orm['dictionary.WordHasSkill']", 'symmetrical': 'False'})
        },
        u'dictionary.wordhasskill': {
            'Meta': {'object_name': 'WordHasSkill', 'db_table': "'dictionary_word_has_skill'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dictionary.Skill']", 'on_delete': 'models.PROTECT', 'db_column': "'skill'"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'value'"}),
            'word': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dictionary.Word']", 'on_delete': 'models.PROTECT', 'db_column': "'word'"})
        }
    }

    complete_apps = ['dictionary']