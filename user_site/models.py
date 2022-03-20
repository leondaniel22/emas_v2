from datetime import datetime

from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.contrib.contenttypes.models import ContentType
from dbview.models import DbView
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Instance(models.Model):
    """model for instances"""

    name = models.CharField(verbose_name=_("Name"), max_length=200)
    routemodel = models.ImageField(verbose_name=_("Routemodel"), upload_to='routemodel/', null=True, blank=True)
    image_map = models.CharField(verbose_name=_("Image-Map"), max_length=1000, null=True, blank=True)
    currently_active = models.BooleanField(verbose_name=_("Active"), default=False)
    created_date = models.DateTimeField(verbose_name=_("Created date"), auto_now_add=True, null=True, blank=True)
    updated_date = models.DateTimeField(verbose_name=_("Changed date"), auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = _("Instance")
        verbose_name_plural = _("Instances")

    # overwrite the save method, to set the currently active instance globally
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.currently_active:
            try:
                tmp = Instance.objects.get(currently_active=True)
                if not self == tmp:
                    tmp.currently_active = False
                    tmp.save()
            except Instance.DoesNotExist:
                pass
        super(Instance, self).save()

    def __str__(self):
        return self.name


class ErrorCategory(models.Model):
    """model for error categories"""

    name = models.CharField(verbose_name=_("Name"), max_length=200)
    description = models.CharField(verbose_name=_("Description"), max_length=500, null=True, blank=True)
    instance = models.ForeignKey(verbose_name=_("Instance"), to=Instance, on_delete=models.SET_NULL, null=True, blank=True)
    created_date = models.DateTimeField(verbose_name=_("Created date"), auto_now_add=True, null=True, blank=True)
    updated_date = models.DateTimeField(verbose_name=_("Changed date"), auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Error category")
        verbose_name_plural = _("Error categories")


class Location(models.Model):
    """model for error locations"""

    name = models.CharField(verbose_name=_("Name"), max_length=200)
    description = models.CharField(verbose_name=_("Description"), max_length=500, null=True, blank=True)
    pdf_document = models.FileField(verbose_name=_("PDF document"), upload_to='locations/', null=True, blank=True)
    instance = models.ForeignKey(verbose_name=_("Instance"), to=Instance, on_delete=models.SET_NULL, null=True, blank=True)
    created_date = models.DateTimeField(verbose_name=_("Created date"), auto_now_add=True, null=True, blank=True)
    updated_date = models.DateTimeField(verbose_name=_("Changed date"), auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")


class ErrorAppearance(models.Model):
    """model for error appearances"""

    name = models.CharField(verbose_name=_("Name"), max_length=200)
    description = models.CharField(verbose_name=_("Description"), max_length=500, null=True, blank=True)
    locations = models.ManyToManyField(verbose_name=_("Location"), to=Location)
    media = models.FileField(verbose_name=_("Image/Video"), upload_to='error_appearances/', default="error_appearances/coming-soon.png", null=True, blank=True, )
    error_category = models.ForeignKey(verbose_name=_("Error category"), to=ErrorCategory, on_delete=models.RESTRICT)
    created_date = models.DateTimeField(verbose_name=_("Created date"), auto_now_add=True, null=True, blank=True)
    updated_date = models.DateTimeField(verbose_name=_("Changed date"), auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name

    # method to get multiple locations for one error appearance
    def get_locations(self):
        return "; ".join([location.name for location in self.locations.all()])

    get_locations.short_description = _("Location")

    class Meta:
        verbose_name = _("Error appearance")
        verbose_name_plural = _("Error appearances")


class Solution(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=500)
    description = models.CharField(verbose_name=_("Description"), max_length=500, null=True, blank=True)
    media = models.FileField(verbose_name=_("Image/Video"), upload_to='solutions/', default="solutions/coming-soon.png", null=True, blank=True)
    rating = models.IntegerField(verbose_name=_("Rating"), default=0)
    error_appearance = models.ForeignKey(verbose_name=_("Error appearance"), to=ErrorAppearance, on_delete=models.RESTRICT)
    created_date = models.DateTimeField(verbose_name=_("Created date"), auto_now_add=True, null=True, blank=True)
    updated_date = models.DateTimeField(verbose_name=_("Changed date"), auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Solution")
        verbose_name_plural = _("Solutions")


class ImportExport(models.Model):
    """pseudo-model for the import/export function"""

    class Meta:
        app_label = 'user_site'
        verbose_name = 'Import/Export'
        verbose_name_plural = 'Import/Export'


class CompleteError(models.Model):
    """pseudo-model for the overview"""

    # overwrite save function
    def save(self, *args, **kwargs):
        instance = Instance.objects.create(self, kwargs)
        instance.save()

    class Meta:
        managed = False
        verbose_name = _("Overview")
        verbose_name_plural = _("Overviews")