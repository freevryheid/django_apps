from django.contrib import admin
from .models import MaterialCategory, MaterialApplication, MaterialSupplier, Material
# from site_auth.admin import SiteOnlyAdmin


@admin.register(MaterialCategory)
class MaterialCategoryAdmin(admin.ModelAdmin):
  pass


@admin.register(MaterialApplication)
class MaterialApplicationAdmin(admin.ModelAdmin):
  pass


@admin.register(MaterialSupplier)
class MaterialSupplierAdmin(admin.ModelAdmin):
# class MaterialSupplierAdmin(SiteOnlyAdmin):
  exclude = ('site',)

  def get_queryset(self, request):
    return MaterialSupplier.on_site.all()


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
  exclude = ('site',)

  def get_queryset(self, request):
    return Material.on_site.all()

# admin.site.register(MaterialSupplier, MaterialSupplierAdmin)

