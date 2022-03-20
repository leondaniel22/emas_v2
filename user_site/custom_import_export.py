import pandas as pd
import tablib
from .models import *
from import_export import resources
from django.utils.translation import ugettext_lazy as _

def extract_import_data(file):
    dict_data = pd.read_excel(file)

    error_categories = dict_data.get("Error category")
    error_appearances = dict_data.get("Error appearance")
    locations = dict_data.get("Location")
    solutions = dict_data.get("Solution")

    rows = dict_data.index.stop
    dataset = tablib.Dataset()
    dataset.headers = ["Error category", "Error appearance", "Location", "Solution"]
    for i in range(rows):
        row = []
        if not pd.isna(error_categories.get(i)):
            error_category = error_categories.get(i)
            exists = ErrorCategory.objects.filter(name=error_category).exists()
            row.append((error_category, exists))
        if not pd.isna(error_appearances.get(i)):
            error_appearance = error_appearances.get(i)
            exists = ErrorAppearance.objects.filter(name=error_appearance).exists()
            row.append((error_appearance, exists))
        if not pd.isna(locations.get(i)):
            locations_ = locations.get(i)
            exists = False
            for location in locations_.split(";"):
                if Location.objects.filter(name=location).exists():
                    exists = True
            row.append((locations_, exists))
        if not pd.isna(solutions.get(i)):
            solution = solutions.get(i)
            exists = Solution.objects.filter(name=solution).exists()
            row.append((solutions.get(i), exists))
        dataset.append(row)
    return dataset


def save_import_data(confirmed_import_data, instance):
    try:
        for row in confirmed_import_data:

            error_category_data = row[0]
            value, exists = error_category_data
            error_category, created = ErrorCategory.objects.get_or_create(name=value.strip(), instance=instance)

            location_data = row[2]
            value, exists = location_data
            locations = []
            for v in value.split(';'):
                location, created = Location.objects.get_or_create(name=v.strip(), instance=instance)
                locations.append(location)

            error_appearance_data = row[1]
            value, exists = error_appearance_data
            error_appearance, created = ErrorAppearance.objects.get_or_create(name=value.strip(), error_category=error_category)
            for location in locations:
                if location not in error_appearance.locations.all():
                    error_appearance.locations.add(location)

            solution_data = row[3]
            value, exists = solution_data
            solution, created = Solution.objects.get_or_create(name=value.strip(), error_appearance=error_appearance)

        return True
    except Exception:
        return False
