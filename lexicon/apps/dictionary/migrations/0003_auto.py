# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field metonymy on 'Word'
        m2m_table_name = db.shorten_name('dictionary_word_metonymy')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('word', models.ForeignKey(orm[u'dictionary.word'], null=False)),
            ('metonymy', models.ForeignKey(orm[u'dictionary.metonymy'], null=False))
        ))
        db.create_unique(m2m_table_name, ['word_id', 'metonymy_id'])

        # Adding M2M table for field semantic_field on 'Word'
        m2m_table_name = db.shorten_name('dictionary_word_semantic_field')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('word', models.ForeignKey(orm[u'dictionary.word'], null=False)),
            ('semanticfield', models.ForeignKey(orm[u'dictionary.semanticfield'], null=False))
        ))
        db.create_unique(m2m_table_name, ['word_id', 'semanticfield_id'])


    def backwards(self, orm):
        # Removing M2M table for field metonymy on 'Word'
        db.delete_table(db.shorten_name('dictionary_word_metonymy'))

        # Removing M2M table for field semantic_field on 'Word'
        db.delete_table(db.shorten_name('dictionary_word_semantic_field'))


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
        u'dictionary.metaphor': {
            'Meta': {'ordering': "['name']", 'object_name': 'Metaphor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'name'"})
        },
        u'dictionary.metonymy': {
            'Meta': {'ordering': "['name']", 'object_name': 'Metonymy'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'name'"})
        },
        u'dictionary.semanticfield': {
            'Meta': {'ordering': "['name']", 'object_name': 'SemanticField', 'db_table': "'dictionary_semantic_field'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'name'"})
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
            'metaphor': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['dictionary.Metaphor']", 'symmetrical': 'False'}),
            'metonymy': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['dictionary.Metonymy']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'name'"}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'db_column': "'order'"}),
            'semantic_field': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['dictionary.SemanticField']", 'symmetrical': 'False'}),
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