from django.core.management.base import BaseCommand
from mat.models import MaterialApplication, MaterialCategory, MaterialSupplier

class Command(BaseCommand):
  args = '<foo bar ...>'
  help = 'our help string comes here'

  def del_material_categories(self):
    MaterialCategory.objects.all().delete()

  def del_material_applications(self):
    MaterialApplication.objects.all().delete()

  def del_material_suppliers(self):
    MaterialSupplier.objects.all().delete()

  def handle(self, *args, **options):
    self.del_material_categories()
    self.del_material_applications()
    self.del_material_suppliers()

