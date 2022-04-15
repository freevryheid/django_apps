from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.db import models
# from django.conf import settings
from django.utils.translation import gettext_lazy as _

class MaterialCategory(models.Model):
  category = models.CharField(max_length=128)

  class Meta:
    verbose_name_plural = 'Material categories'

  def __str__(self):
    return self.category

class MaterialApplication(models.Model):
  application = models.CharField(max_length=128)

  def __str__(self):
    return self.application


class MaterialSupplier(models.Model):
  supplier = models.CharField(max_length=128)
  site = models.ForeignKey(Site, default=Site.objects.get_current().id, on_delete=models.CASCADE)
  objects = models.Manager()
  on_site = CurrentSiteManager()

  def __str__(self):
    return self.supplier


class Material(models.Model):
  code = models.CharField(max_length=128)
  category = models.ForeignKey(MaterialCategory, on_delete=models.CASCADE)
  application = models.ForeignKey(MaterialApplication, on_delete=models.CASCADE)
  supplier = models.ForeignKey(MaterialSupplier, on_delete=models.CASCADE)
  description = models.CharField(max_length=128)
  site = models.ForeignKey(Site, default=Site.objects.get_current().id, on_delete=models.CASCADE)
  objects = models.Manager()
  on_site = CurrentSiteManager()

  def __str__(self):
    return self.code

