import os
from django.contrib.admin import SimpleListFilter
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, redirect
from import_export.admin import ExportMixin
from emas_v2 import settings
from .import_export_resources import *
from .custom_import_export import *
from .forms import *
from django.contrib import admin, messages
import pandas as pd
from django.utils.translation import ugettext_lazy as _


class ErrorDetectionAdminSite(admin.AdminSite):
    """
        class for the admin-site. Implemented to add additional urls,
        ,so that custom views and html-pages can be rendered
    """
    site_header = _("Website management")
    site_title = _("Website management")
    index_title = _("Website management")

    # urls for custom vies and html-pages
    def get_urls(self):
        urls = super(ErrorDetectionAdminSite, self).get_urls()
        custom_urls = [
            path('admin/import_export_data/', self.admin_view(import_export_data), name="import_export_data"),
            path('admin/import_data_confirm/', self.admin_view(import_data_confirm), name="import_data_confirm"),
            path('admin/import_data_save/', self.admin_view(import_data_save), name="import_data_save"),
            path('admin/export_data/', self.admin_view(export_data), name="export_data"),
            path('admin/image_map_creator/<int:instance_id>', self.admin_view(image_map_creator),
                 name="image_map_creator"),
            path('admin/add_image_map/<int:instance_id>', self.admin_view(add_image_map),
                 name="add_image_map"),
            path('admin/template/', self.admin_view(template),
                 name="template"),
        ]
        return custom_urls + urls


# register the custom admin class
error_detection_admin_site = ErrorDetectionAdminSite(name="error_detection_admin")


@admin.register(Instance, site=error_detection_admin_site)
class InstanceAdmin(admin.ModelAdmin):
    """class that shows the instance model at the admin page"""

    list_display = ("name", "routemodel", "currently_active", "created_date", "updated_date")
    readonly_fields = ("image_map", )

    change_form_template = "admin/change_form_instance.html"
    add_form_template = ""


def image_map_creator(request, instance_id):
    """function that lets user create a custom image map for the dashboard"""
    instance = Instance.objects.get(id=instance_id)
    locations = Location.objects.filter(instance=instance)
    map_creator_form = MapCreatorForm(locations=locations)
    image_map_form = ImageMapForm()

    return render(request, 'admin/image_map_creator.html',
                  {
                      'title': u'Image Map Creator',
                      'instance': instance,
                      'map_creator_form': map_creator_form,
                      'image_map_form': image_map_form,
                  }
                  )


def add_image_map(request, instance_id):
    """function that adds the custom created image map to an instance"""
    instance = Instance.objects.get(id=instance_id)
    if request.method == 'POST':
        form = ImageMapForm(request.POST)
        if form.is_valid():
            image_map = request.POST.get('image_map')
            instance.image_map = image_map
            instance.save()
    else:
        form = ImageMapForm()

    return HttpResponseRedirect('../../' + Instance._meta.app_label + '/' + Instance._meta.model_name + '/' + str(instance_id) +'/change')


@admin.action(description=_("Change the related instance"))
def change_instances(modeladmin, request, queryset):
    """
        function that allows user to add the instance of multiple elements at once
        (only for error categories and locations)
    """

    if 'do_action' in request.POST:
        form = ChangeInstanceForm(request.POST)
        if form.is_valid():
            instance = form.cleaned_data['instance']
            updated = queryset.update(instance=instance)
            messages.success(request, ('{0} ' + _('Instance successfully changed')).format(updated))
            return
    else:
        form = ChangeInstanceForm()

    return render(request, 'admin/action_instance.html',
                  {
                      'title': _('Choose instance'),
                      'objects': queryset,
                      'form': form
                  }
                  )


@admin.register(ErrorCategory, site=error_detection_admin_site)
class ErrorCategoryAdmin(admin.ModelAdmin):
    """class that shows the error category model at the admin page"""

    resource_class = ErrorCategoryResource
    list_display = ("name", "description", "created_date", "updated_date")
    list_filter = ('instance',)
    actions = [change_instances]

    def get_import_form(self):
        return CompleteErrorImportForm

    def get_confirm_import_form(self):
        return CompleteErrorConfirmInputForm

    def get_resource_kwargs(self, request, *args, **kwargs):
        rk = super().get_resource_kwargs(request, *args, **kwargs)
        rk['request'] = request
        return rk


@admin.register(Location, site=error_detection_admin_site)
class LocationAdmin(admin.ModelAdmin):
    """class that shows the location model at the admin page"""

    resource_class = LocationResource
    list_display = ("name", "description", "created_date", "updated_date")
    list_filter = ('instance',)
    actions = [change_instances]


@admin.register(ErrorAppearance, site=error_detection_admin_site)
class ErrorAppearanceAdmin(admin.ModelAdmin):
    """class the show the error appearance model at the admin page"""

    resource_class = ErrorAppearanceResource
    list_display = ("name", "description", "get_locations", "error_category", "created_date", "updated_date")
    list_filter = ('error_category__instance', 'locations', 'error_category', ('media', admin.EmptyFieldListFilter))

    def get_import_form(self):
        return CompleteErrorImportForm

    def get_confirm_import_form(self):
        return CompleteErrorConfirmInputForm

    def get_resource_kwargs(self, request, *args, **kwargs):
        rk = super().get_resource_kwargs(request, *args, **kwargs)
        rk['request'] = request
        return rk


def custom_titled_filter(title):
    """fucntion for adding a custom filter"""

    class Wrapper(admin.FieldListFilter):
        """Wrapper class"""
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance

    return Wrapper


@admin.register(Solution, site=error_detection_admin_site)
class SolutionAdmin(admin.ModelAdmin):
    """class that shows the solution model at the admin page"""
    resource_class = SolutionResource
    list_display = ("name", "description", "rating", "error_appearance", "created_date", "updated_date")
    list_filter = ('error_appearance__error_category__instance', 'error_appearance__locations',
                   ('error_appearance__error_category__name', custom_titled_filter(_('Error category'))),
                   ('media', admin.EmptyFieldListFilter))

    def get_import_form(self):
        return CompleteErrorImportForm

    def get_confirm_import_form(self):
        return CompleteErrorConfirmInputForm

    def get_resource_kwargs(self, request, *args, **kwargs):
        rk = super().get_resource_kwargs(request, *args, **kwargs)
        rk['request'] = request
        return rk


def import_export_data(request):
    """Rendering the html-page that let users import/export the database content"""

    title = "Excel Import/Export"
    upload_form = UploadForm()
    instance_form = InstanceForm()

    return render(
        request,
        'admin/import_export_data.html',
        {
            'title': title,
            'has_permission': True,
            'upload_form': upload_form,
            'instance_form': instance_form,
        }
    )


def import_data_confirm(request):
    """Rendering the confirmation html-page of the import function"""

    title = "Import"
    dataset = None
    instance = None
    confirm_instance_form = ConfirmInstanceForm()
    if request.method == "POST":
        upload_form = UploadForm(request.POST, request.FILES)
        instance_form = InstanceForm(request.POST)
        if upload_form.is_valid():
            upload_file = request.FILES['upload_file']
            instance_id = request.POST.get('instance')
            instance = Instance.objects.get(id=instance_id)
            dataset = extract_import_data(upload_file)
            confirmed_import_data = []
            for row in dataset:
                confirmed_import_data.append(row)
            request.session['confirmed_import_data'] = confirmed_import_data
            # still in production
    else:
        upload_form = UploadForm()
        instance_form = InstanceForm()
    return render(
        request,
        'admin/import_data_confirm.html',
        {
            'title': title,
            'has_permission': True,
            'dataset': dataset,
            'instance': instance,
            'confirm_instance_form': confirm_instance_form,
        }
    )


def import_data_save(request):
    """saving the imports into the data base after successful confirmation"""

    if request.method == "POST":
        confirm_instance_form = ConfirmInstanceForm(request.POST)
        if confirm_instance_form.is_valid():
            instance_id = request.POST.get('instance')
            instance = Instance.objects.get(id=instance_id)
            confirmed_import_data = request.session.get('confirmed_import_data')
            successful = save_import_data(confirmed_import_data, instance)
            if not successful:
                return HttpResponse(_("Data could not be imported, please contact your Administrator"))
    else:
        confirm_instance_form = ConfirmInstanceForm()

    return redirect('admin:index')


def export_data(request):
    """adding all the databse content into a xlsx-file and let the user download it"""

    file_path = os.path.join(settings.MEDIA_ROOT, "export_files/export.xlsx")
    if request.method == "POST":
        instance_form = InstanceForm(request.POST)
        if instance_form.is_valid():
            instance_id = request.POST.get('instance')
            instance = Instance.objects.get(pk=instance_id)
            queryset = Solution.objects.select_related('error_appearance',
                                                   'error_appearance__error_category'
                                                   ).filter(error_appearance__error_category__instance=instance_id)
            rows = []
            for element in queryset:
                error_category = element.error_appearance.error_category.name
                error_appearance = element.error_appearance.name
                locations_queryset = element.error_appearance.locations.all()
                locations = []
                for location_element in locations_queryset:
                    locations.append(location_element.name)
                solution = element.name
                row = [error_category, error_appearance, ";".join(locations), solution]
                rows.append(row)
            dataframe = pd.DataFrame(rows, columns=[_("Error category"), _("Error appearance"), _("Location"), _("Solution")])
            dataframe.to_excel(file_path, index=False )

            if os.path.exists(file_path):
                with open(file_path, 'rb') as fh:
                    response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                    return response
            raise Http404

    return redirect('../../import_export_data.html')


def template(request):

    file_path = os.path.join(settings.MEDIA_ROOT, "export_files/template.xlsx")
    dataframe = pd.DataFrame([], columns=[_("Error category"), _("Error appearance"), _("Location"), _("Solution")])
    dataframe.to_excel(file_path, index=False )

    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response

    return redirect('../../import_export_data.html')


@admin.register(ImportExport, site=error_detection_admin_site)
class ImportExportAdmin(admin.ModelAdmin):
    """class that shows the custom Import/Export function at the admin page"""

    def get_urls(self):
        view = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)

        return [
            path('admin/', import_export_data, name=view),
        ]


class OverviewInstanceFilter(SimpleListFilter):
    """
        class for filtering the elements by instance
        (only for error categories and locations)
    """

    title = _("Instances")
    parameter_name = "instance"
    default_value = None

    def lookups(self, request, model_admin):
        list_of_instances = []
        queryset = Instance.objects.all()
        for instance in queryset:
            list_of_instances.append((str(instance.id), instance.name))
        return sorted(list_of_instances, key=lambda x: x[1])

    def queryset(self, request, queryset):
        if self.value():
            queryset = Solution.objects.select_related('error_appearance', 'error_appearance__error_category'). \
                filter(error_appearance__error_category__instance=self.value())
        return queryset


class OverviewLocationFilter(SimpleListFilter):
    """
        class for filtering the elements by instance
        (only for error appearances)
    """

    title = _("Locations")
    parameter_name = "locations"
    default_value = None

    def lookups(self, request, model_admin):
        list_of_locations = []
        queryset = Location.objects.all()
        for location in queryset:
            list_of_locations.append((str(location.id), location.name))
        return sorted(list_of_locations, key=lambda x: x[1])

    def queryset(self, request, queryset):
        if self.value():
            queryset = Solution.objects.select_related('error_appearance', 'error_appearance__error_category'). \
                filter(error_appearance__locations=self.value())
        return queryset


@admin.register(CompleteError, site=error_detection_admin_site)
class CompleteErrorAdmin(admin.ModelAdmin):
    """class that shows the pseudo-model complete error (overview) at the admin page"""

    add_form_template = "admin/overview_add_template.html"
    list_display = ("get_error_category", "get_error_appearance", "get_locations", "get_solution")
    list_filter = (OverviewInstanceFilter, OverviewLocationFilter,)

    def get_error_category(self, obj):
        return obj.error_appearance.error_category.name

    def get_error_appearance(self, obj):
        return obj.error_appearance.name

    def get_locations(self, obj):
        return obj.error_appearance.get_locations()

    def get_solution(self, obj):
        return obj.name

    def get_instance(self, obj):
        return obj.error_appearance.error_category.instance

    get_error_category.short_description = _("Error category")
    get_error_appearance.short_description = _("Error appearance")
    get_locations.short_description = _("Location")
    get_solution.short_description = _("Solution")
    get_instance.short_description = _("Related Instance")

    def get_queryset(self, request):
        qs = Solution.objects.select_related('error_appearance', 'error_appearance__error_category')
        return qs

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


def get_app_list(self, request):
    """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        (also the ones from the nlp-component and the users and groups from django)
    """
    ordering = {
        _("Overview"): 1,
        _("Import/Export"): 2,
        _("Instances"): 3,
        _("Location"): 4,
        _("Error category"): 5,
        _("Error appearances"): 6,
        _("Solutions"): 7,
        _("Excel Import"): 8,
        _("Themes"): 9,
        _("Groups"): 10,
        _("User"): 11,
        _("Authentications"): 12,
        _("New user comments"): 13,
        _("Groups of user comments"): 14,
        _("similarity threshold"): 15,

    }
    app_dict = self._build_app_dict(request)
    # a.sort(key=lambda x: b.index(x[0]))

    # Sort the apps alphabetically.
    app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

    # Sort the models alphabetically within each app.
    for app in app_list:
        app['models'].sort(key=lambda x: ordering[x['name']])

    return app_list


# adding the custom sorting to the admin site
#admin.AdminSite.get_app_list = get_app_list
