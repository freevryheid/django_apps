from django.contrib import admin
from .models import QualificationAgency, QualificationLevel, QualificationTest, Technician


@admin.register(QualificationAgency)
class QualificationAgencyAdmin(admin.ModelAdmin):
  pass


@admin.register(QualificationLevel)
class QualificationLevelAdmin(admin.ModelAdmin):
  fields = ('level', 'agency')
  list_display = ['level', 'agency']


@admin.register(QualificationTest)
class QualificationTestAdmin(admin.ModelAdmin):
  pass


@admin.register(Technician)
class TechnicianAdmin(admin.ModelAdmin):
  fields = ('name', 'level', 'authorization_date', 'expiration_date')
  list_display = ['name', 'level', 'authorization_date', 'expiration_date']
