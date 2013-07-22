# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Place'
        db.create_table(u'guide_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('overview', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'guide', ['Place'])

        # Adding model 'Photo'
        db.create_table(u'guide_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guide.Place'])),
        ))
        db.send_create_signal(u'guide', ['Photo'])

        # Adding model 'Program'
        db.create_table(u'guide_program', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guide.Place'])),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('for_credit', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'guide', ['Program'])

        # Adding model 'Tip'
        db.create_table(u'guide_tip', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guide.Place'], null=True)),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guide.Program'], null=True)),
        ))
        db.send_create_signal(u'guide', ['Tip'])


    def backwards(self, orm):
        # Deleting model 'Place'
        db.delete_table(u'guide_place')

        # Deleting model 'Photo'
        db.delete_table(u'guide_photo')

        # Deleting model 'Program'
        db.delete_table(u'guide_program')

        # Deleting model 'Tip'
        db.delete_table(u'guide_tip')


    models = {
        u'guide.photo': {
            'Meta': {'object_name': 'Photo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guide.Place']"})
        },
        u'guide.place': {
            'Meta': {'object_name': 'Place'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'overview': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'guide.program': {
            'Meta': {'object_name': 'Program'},
            'for_credit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guide.Place']"})
        },
        u'guide.tip': {
            'Meta': {'object_name': 'Tip'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guide.Place']", 'null': 'True'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guide.Program']", 'null': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['guide']