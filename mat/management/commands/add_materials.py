from django.core.management.base import BaseCommand
from mat.models import MaterialApplication, MaterialCategory, MaterialSupplier

class Command(BaseCommand):
  args = '<foo bar ...>'
  help = 'our help string comes here'

  def add_material_categories(self):
    material_category = [
      'Aggregate',
      'Complete mixture',
      'Cuts and fills',
      'Coarse aggregate',
      'Combined aggregate',
      'Fine aggregate',
      'Mineral filler',
      'Non-structural complete mixture',
      'Structural complete mixture',
      'Pavement complete mixture',
      'Roadway',
      'RAP',
      'Select',
      'Non-select',
      'New',
    ]

    for cat in material_category:
      c = MaterialCategory(category=cat)
      c.save()

  def add_material_applications(self):
    material_application = [
      'Asphalt Stabilized Base (ASB)',
      'Embankment',
      'HCC',
      'LRA/HMCL ACP',
      'Method ACP',
      'QCQA ACP',
      'Retaining wall',
      'Surface treatment',
      'Treated subgrade',
      'Treated base course',
      'Untreated base course',
    ]

    for app in material_application:
      a = MaterialApplication(application=app)
      a.save()

  def add_material_suppliers(self):
    material_supplier = [
      'Cemex-Baytown Plant',
      'Morgan Pit',
      'Weldon Alders Borrow Source',
      'Argos Ready Mix',
      'Hanson-Bristol',
      'Lattimore-Rosser',
      'Lattimore-Ambrose',
      'Hanson-Perch Hill',
      'Hanson-Lake Bridgeport',
      'Lattimore-Stringtown',
      'Lattimore (LMC)',
      'ROW',
      'Pegasus Link Constructors',
      'Martin Marietta',
      'Lattimore, N Dallas Plant',
      'Arcosa-Cottonwood',
      'F & H Construction-SG',
      'Martin Marietta-Bridgeport',
      'Arcosa-Asa Pitt',
      'Argos Ready Mix-101',
      'Argos Ready Mix-130',
      'Lattimore Materials-955',
      'Lattimore Materials-950',
      'PLC-999',
      'Martin Marietta-138',
      'Lattimore Materials-964',
      'Martin Marietta-Midlothian',
      'Martin Marietta-Mill Creek',
      'Hanson-Bristol 2',
      'Big City Crushed Concrete',
      'H&H Concrete-999',
      'PLC-002',
      'TXBIT - Terrell Plant',
      'Big D Ready Mix Concrete',
      'Pine Street Borrow',
    ]

    for sup in material_supplier:
      s = MaterialSupplier(supplier=sup)
      s.save()

  def handle(self, *args, **options):
    # self.add_material_categories()
    # self.add_material_applications()
    self.add_material_suppliers()


