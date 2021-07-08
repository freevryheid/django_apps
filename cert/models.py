from django.db import models


class QualificationAgency(models.Model):
  agency = models.CharField(max_length=128, unique=True)

  class Meta:
    verbose_name_plural = 'Qualification agencies'

  def __str__(self):
    return self.agency


class QualificationLevel(models.Model):
  level = models.CharField(max_length=128, unique=True)
  agency = models.ForeignKey(QualificationAgency, on_delete=models.CASCADE)

  def __str__(self):
    return self.level


class QualificationTest(models.Model):
  test = models.CharField(max_length=128, unique=True)
  level = models.ForeignKey(QualificationLevel, on_delete=models.CASCADE)

  def __str__(self):
    return self.test


class Technician(models.Model):
  name = models.CharField(max_length=128)
  email = models.EmailField()
  level = models.ForeignKey(QualificationLevel, on_delete=models.CASCADE)
  authorization_date = models.DateField()
  expiration_date = models.DateField()
  certificate = models.FileField(upload_to='I2MS/static/', blank=True)

  def __str__(self):
    return self.name


