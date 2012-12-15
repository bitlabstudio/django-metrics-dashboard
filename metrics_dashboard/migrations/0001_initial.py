# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DashboardWidgetSettings'
        db.create_table('metrics_dashboard_dashboardwidgetsettings', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('widget_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('setting_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=4000)),
        ))
        db.send_create_signal('metrics_dashboard', ['DashboardWidgetSettings'])

        # Adding unique constraint on 'DashboardWidgetSettings', fields ['widget_name', 'setting_name']
        db.create_unique('metrics_dashboard_dashboardwidgetsettings', ['widget_name', 'setting_name'])


    def backwards(self, orm):
        # Removing unique constraint on 'DashboardWidgetSettings', fields ['widget_name', 'setting_name']
        db.delete_unique('metrics_dashboard_dashboardwidgetsettings', ['widget_name', 'setting_name'])

        # Deleting model 'DashboardWidgetSettings'
        db.delete_table('metrics_dashboard_dashboardwidgetsettings')


    models = {
        'metrics_dashboard.dashboardwidgetsettings': {
            'Meta': {'unique_together': "(('widget_name', 'setting_name'),)", 'object_name': 'DashboardWidgetSettings'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'setting_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '4000'}),
            'widget_name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['metrics_dashboard']