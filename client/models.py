from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError(_('An email address is required'))
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        if kwargs.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if kwargs.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **kwargs)

from django.core.mail import send_mail

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=False)
    site = models.ForeignKey(Site, default=settings.SITE_ID, on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    default_manager = CustomUserManager()
    on_site = CurrentSiteManager()

    class Meta:
        unique_together = ('site', 'email')
        verbose_name = 'user'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def email_user(self, subject, message, from_email=settings.EMAIL_HOST_USER, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


from django.db.models.signals import pre_save
from django.dispatch import receiver

@receiver(pre_save, sender=CustomUser)
def compose_username(sender, instance, **kwargs):
    site_id = instance.site_id or 1
    instance.username = "{0}__{1}".format( instance.email, site_id )

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class SiteBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        site = kwargs.get('site', settings.SITE_ID)
        identifier = "{0}__{1}".format( username, site )
        try:
            user = UserModel.objects.get(username=identifier)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        return None

from django.contrib.auth.models import Group

class CustomGroup(Group):

    class Meta:
        proxy = True
        verbose_name = 'group'

class CustomSite(Site):

    class Meta:
        proxy = True
        verbose_name = 'site'

