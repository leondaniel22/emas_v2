from django.urls import path
from import_export.widgets import ForeignKeyWidget
from .forms import *
from .admin import *
from import_export.admin import ImportExportModelAdmin, ImportMixin
from import_export import resources
import import_export
from import_export.fields import Field
import tablib
from import_export.admin import ImportExportModelAdmin
from django.utils.translation import ugettext_lazy as _


class ErrorCategoryResource(resources.ModelResource):
    name = Field(column_name=_("Error category"), attribute="name")
    description = Field(column_name=_("Description"), attribute="description")
    instance = Field(column_name=_("Instance"), attribute="instance")

    def __init__(self, request=None):
        super()
        self.request = request

    def before_import_row(self, row, **kwargs):
        instance_id = self.request.POST.get('instance')
        instance = Instance.objects.get(id=instance_id)
        row['Instanz'] = instance

    class Meta:
        model = ErrorCategory
        exclude = ('id',)
        import_id_fields = ('name',)
        fields = ('name', 'description', 'instance')


class LocationResource(resources.ModelResource):
    name = Field(column_name=_("Location"), attribute="name")
    description = Field(column_name=_("Description"), attribute="description")

    def __init__(self, request=None):
        super()
        self.request = request

    def before_import_row(self, row, **kwargs):
        instance_id = self.request.POST.get('instance')
        instance = Instance.objects.get(id=instance_id)
        row['Instanz'] = instance

    class Meta:
        model = ErrorAppearance
        exclude = ('id',)
        import_id_fields = ('name',)
        fields = ('name', 'description')


class ErrorAppearanceResource(resources.ModelResource):
    name = Field(column_name=_("Error appearance"), attribute="name")
    description = Field(column_name=_("Description"), attribute="description")
    location = Field(column_name=_("Location"), attribute="location", widget=ForeignKeyWidget(Location, "name"))
    error_category = Field(column_name=_("Error category"), attribute="error_category",
                           widget=ForeignKeyWidget(ErrorCategory, "name"))

    def __init__(self, request=None):
        super()
        self.request = request

    def before_import_row(self, row, **kwargs):
        instance_id = self.request.POST.get('instance')
        instance = Instance.objects.get(id=instance_id)
        row['Instanz'] = instance

    class Meta:
        model = ErrorAppearance
        exclude = ('id',)
        import_id_fields = ('name',)
        fields = ('name', 'description', 'location', 'error_category', 'instance')


class SolutionResource(resources.ModelResource):
    name = Field(column_name=_("Solution"), attribute="name")
    description = Field(column_name=_("Description"), attribute="description")
    error_appearance = Field(column_name=_("Error appearance"), attribute="error_appearance",
                             widget=ForeignKeyWidget(ErrorAppearance, "name"))

    def __init__(self, request=None):
        super()
        self.request = request

    def before_import_row(self, row, **kwargs):
        instance_id = self.request.POST.get('instance')
        instance = Instance.objects.get(id=instance_id)
        row['Instanz'] = instance

    class Meta:
        model = Solution
        exclude = ('id',)
        import_id_fields = ('name',)
        fields = ('name', 'description', 'error_appearance', 'instance')



