from django.contrib import admin
from .models import MaterialCategory, MaterialApplication, MaterialSupplier, Material


@admin.register(MaterialCategory)
class MaterialCategoryAdmin(admin.ModelAdmin):
  pass


@admin.register(MaterialApplication)
class MaterialApplicationAdmin(admin.ModelAdmin):
  pass


@admin.register(MaterialSupplier)
class MaterialSupplierAdmin(admin.ModelAdmin):
  pass


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
  pass


