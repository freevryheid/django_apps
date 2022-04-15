from django.contrib import admin
from .models import QualificationAgency, QualificationLevel, QualificationTest, QualificationTestSeries, QualificationCertificate, Technician
from datetime import date, timedelta
from django.utils.translation import gettext_lazy as _

@admin.register(QualificationAgency)
class QualificationAgencyAdmin(admin.ModelAdmin):
  fields = ('agency', 'desc',)
  list_display = ('agency', 'desc',)

@admin.register(QualificationLevel)
class QualificationLevelAdmin(admin.ModelAdmin):
  fields = ('level', 'desc', 'agency', 'tests')
  list_display = ('level', 'desc', 'agency',)
  list_filter = ('agency',)

@admin.register(QualificationTest)
class QualificationTestAdmin(admin.ModelAdmin):
  # fields = ('test', 'desc', 'levels')
  fields = ('test', 'desc')
  list_display = ('test', 'desc',)
  # list_filter = ['levels']

@admin.register(QualificationTestSeries)
class QualificationTestSeriesAdmin(admin.ModelAdmin):
  fields = ('series', 'desc', 'tests')
  list_display = ('series', 'desc',)
  list_filter = ('tests',)

class ExpiredCertsFilter(admin.SimpleListFilter):
  title = _('Expired')
  parameter_name = 'expired'

  def lookups(self, request, model_admin):
    return (
      ('today','today'),
      ('month', 'in a month from today'),)

  def queryset(self, request, queryset):
    if self.value() == None:
      return queryset

    if self.value() == 'today':
      today = date.today()
      return queryset.filter(expiration_date__lte=today)

    else:
      today = date.today()
      return queryset.filter(expiration_date__lte=(today + timedelta(days=30)))

class TestsFilter(admin.SimpleListFilter):
  title = _('Tests')
  parameter_name = 'level'

  def lookups(self, request, model_admin):
    alltests = set([t for t in QualificationTest.objects.all()])
    return [(t.id, t.test) for t in alltests]

  def queryset(self, request, queryset):
    if self.value() == None:
      return queryset
    else:
      return queryset.filter(level__tests=self.value())

@admin.register(QualificationCertificate)
class QualificationCertificateAdmin(admin.ModelAdmin):
  # today = date.today()
  fields = ('technician', 'level', 'authorization_date', 'expiration_date', 'certificate')
  list_display = ('technician', 'level', 'authorization_date', 'expiration_date', 'certificate',)
  list_filter = ('technician__name', 'level__level', ExpiredCertsFilter, TestsFilter,)

# @admin.register(CertificateInLine)
class CertificateInLine(admin.TabularInline):
  model = QualificationCertificate
  classes = ['collapse']

@admin.register(Technician)
class TechnicianAdmin(admin.ModelAdmin):
  fields = ('name', 'email', 'firm')
  list_display = ('name', 'email', 'firm',)
  inlines = [CertificateInLine]
  # list_filter = (TestsFilter,)
  # fields = ('name', 'level', 'authorization_date', 'expiration_date')
  # list_display = ['name', 'level', 'authorization_date', 'expiration_date']




