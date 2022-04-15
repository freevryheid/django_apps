from django.db import models

class QualificationAgency(models.Model):
  agency = models.CharField(max_length=10, unique=True)
  desc = models.CharField('description',max_length=128, blank=True)

  class Meta:
    verbose_name_plural = 'Agencies'

  def __str__(self):
    return self.agency

class QualificationTest(models.Model):
  test = models.CharField(max_length=128)
  desc = models.CharField('description',max_length=128, blank=True)

  class Meta:
    verbose_name_plural = 'Tests'

  def __str__(self):
    return self.test

class QualificationLevel(models.Model):
  level = models.CharField(max_length=128)
  desc = models.CharField('description', max_length=128, blank=True)
  agency = models.ForeignKey(QualificationAgency, on_delete=models.CASCADE)
  tests = models.ManyToManyField(QualificationTest, related_name='levels')

  class Meta:
    verbose_name_plural = 'Levels'

  def __str__(self):
    return self.level

class QualificationTestSeries(models.Model):
  series = models.CharField(max_length=128)
  desc = models.CharField('description', max_length=128, blank=True)
  tests = models.ManyToManyField(QualificationTest)

  class Meta:
    verbose_name_plural = 'Series'

  def __str__(self):
    return self.series

class Technician(models.Model):
  name = models.CharField(max_length=128)
  email = models.EmailField(blank=True)
  firm = models.CharField(max_length=128, blank=True)

  def __str__(self):
    return self.name

class QualificationCertificate(models.Model):
  technician = models.ForeignKey(Technician, on_delete=models.CASCADE)
  level = models.ForeignKey(QualificationLevel, on_delete=models.CASCADE)
  authorization_date = models.DateField()
  expiration_date = models.DateField()
  certificate = models.FileField(upload_to='I2MS/static/', blank=True)

  class Meta:
    verbose_name_plural = 'Certificates'


