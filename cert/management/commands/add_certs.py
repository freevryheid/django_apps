from django.core.management.base import BaseCommand
from cert.models import QualificationAgency, QualificationLevel, QualificationTest, Technician
# from django.conf import settings
# from django.contrib.sites.models import Site

class Command(BaseCommand):
  args = '<foo bar ...>'
  help = 'our help string comes here'

  def add_qualification_agency(self):
    qualification_agency = [
      ['HMAC', 'Hot-Mix Asphalt Center',             ],
      ['ACI', 'American Concrete Institute',        ],
      ['TxDOT', 'Texas Department of Transportation', ],
    ]

    for agy in qualification_agency:
      a = QualificationAgency(agency=agy[0], desc=agy[1])
      a.save()

  def add_qualification_level(self):
    qualification_level = [
      ['ACI 1', 'ACI Concrete Field Testing Technician Grade 1',     'ACI'],
      ['ACI 2', 'ACI Concrete Strength Testing Technician',          'ACI'],
      ['ACI 3', 'ACI Concrete Aggregate Testing Technician Level 1', 'ACI'],
      ['HMA 1', 'TxAPA HMA Plant Mix Specialist Level 1A',           'HMAC'],
      ['HMA 2', 'TxAPA HMA Roadway Specialist Level 1B',             'HMAC'],
      ['HMA 3', 'TxAPA HMA Mix Design Specialist Level 2',           'HMAC'],
      ['HMA 4', 'TxAPA Properties Specialist SB101',                 'HMAC'],
      ['HMA 5', 'TxAPA Field Specialist SB102',                      'HMAC'],
      ['HMA 6', 'TxAPA Material Analysis Specialist SB103',          'HMAC'],
      ['HMA 7', 'TxAPA Strength Spacialist SB201',                   'HMAC'],
      ['HMA 8', 'TxAPA Compressive Strength Specialist SB202',       'HMAC'],
    ]

    for lvl in qualification_level:
      a = QualificationAgency.objects.get(agency=lvl[2])
      l = QualificationLevel(level=lvl[0], desc=lvl[1], agency=a)
      l.save()

  def add_qualification_test(self):
    qualification_test = [
      ['Tex-107-F',           'HMA 3'],
      ['Tex-203-F',           'HMA 3'],
      ['Tex-204-F',           'HMA 3'],
      ['Tex-205-F',           'HMA 3'],
      ['Tex-206-F',           'HMA 3'],
      ['Tex-207-F Part I',    'HMA 3'],
      ['Tex-207-F Part VI',   'HMA 3'],
      ['Tex-207-F Part VIII', 'HMA 3'],
      ['Tex-217-F',           'HMA 3'],
      ['Tex-226-F',           'HMA 3'],
      ['Tex-227-F Part I',    'HMA 3'],
      ['Tex-227-F Part II',   'HMA 3'],
      ['Tex-235-F',           'HMA 3'],
      ['Tex-236-F',           'HMA 3'],
      ['Tex-241-F',           'HMA 3'],
      ['Tex-242-F',           'HMA 3'],
      ['Tex-245-F',           'HMA 3'],
      ['Tex-280-F',           'HMA 3'],
      ['Tex-408-A',           'HMA 3'],
      ['Tex-460-A',           'HMA 3'],
      ['Tex-461-A',           'HMA 3'],
      ['Tex-200-F Part I',    'HMA 1'],
      ['Tex-200-F Part II',   'HMA 1'],
      ['Tex-204-F VMA',       'HMA 1'],
      ['Tex-206-F Part I',    'HMA 1'],
      ['Tex-207-F Part I',    'HMA 1'],
      ['Tex-207-F Part VI',   'HMA 1'],
      ['Tex-207-F Part VIII', 'HMA 1'],
      ['Tex-212-F Part II',   'HMA 1'],
      ['Tex-221-F',           'HMA 1'],
      ['Tex-222-F',           'HMA 1'],
      ['Tex-225-F Part I',    'HMA 1'],
      ['Tex-226-F',           'HMA 1'],
      ['Tex-227-F',           'HMA 1'],
      ['Tex-233-F',           'HMA 1'],
      ['Tex-235-F',           'HMA 1'],
      ['Tex-236-F Part I',    'HMA 1'],
      ['Tex-241-F',           'HMA 1'],
      ['Tex-242-F',           'HMA 1'],
      ['Tex-245-F',           'HMA 1'],
      ['Tex-251-F',           'HMA 1'],
      ['Tex-500-C Part I',    'HMA 1'],
      ['Tex-500-C Part II',   'HMA 1'],
      ['Tex-500-C Part III',  'HMA 1'],
      ['Tex-500-C Part IX',   'HMA 1'],
      ['Tex-530-C',           'HMA 1'],
      ['Tex-100-E',           'HMA 5'],
      ['Tex-101-E Part III',  'HMA 5'],
      ['Tex-103-E',           'HMA 5'],
      ['Tex-115-E Part I',    'HMA 5'],
      ['Tex-140-E',           'HMA 5'],
      ['Tex-400-A',           'HMA 5'],
      ['Tex-600-J Part I',    'HMA 5'],
      ['Tex-207-F Part IV',   'HMA 2'],
      ['Tex-207-F Part V',    'HMA 2'],
      ['Tex-207-F Part VI',   'HMA 2'],
      ['Tex-207-F Part VII',  'HMA 2'],
      ['Tex-207-F Part VIII', 'HMA 2'],
      ['Tex-222-F',           'HMA 2'],
      ['Tex-225-F Part II',   'HMA 2'],
      ['Tex-244-F',           'HMA 2'],
      ['Tex-246-F',           'HMA 2'],
      ['Tex-500-C Part II',   'HMA 2'],
      ['Tex-500-C Part III',  'HMA 2'],
      ['Tex-251-F',           'HMA 2'],
    ]

    for tst in qualification_test:
      l = QualificationLevel.objects.get(level=tst[1])
      t = QualificationTest(test=tst[0], level=l)
      t.save()

  def handle(self, *args, **options):
    self.add_qualification_agency()
    self.add_qualification_level()
    self.add_qualification_test()

