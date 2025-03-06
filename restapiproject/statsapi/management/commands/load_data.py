import os
import csv
from django.core.management.base import BaseCommand
from django.conf import settings
from statsapi.models import Student, Placement, PlacementApplication
#added so that it can be handled directly using manage.py
class Command(BaseCommand):
    help = "Load data from CSV files into PostgreSQL"

    def handle(self, *args, **kwargs):
        data_dir = os.path.join(settings.BASE_DIR, 'statsapi', 'data')#setting data dir for fetching .csv files

        students_csv = os.path.join(data_dir, 'students.csv')
        with open(students_csv, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Student.objects.get_or_create(
                    id=row['id'],
                    rollno=row['rollno'],
                    batch=row['batch'],
                    branch=row['branch']
                )

        placements_csv = os.path.join(data_dir, 'placements.csv')
        with open(placements_csv, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Placement.objects.get_or_create(
                    id=row['id'],
                    name=row['name'],
                    role=row['role'],
                    ctc=row['ctc']
                )

        applications_csv = os.path.join(data_dir, 'placement_applications.csv')
        with open(applications_csv, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                PlacementApplication.objects.get_or_create(
                    id=row['id'],
                    placement_id=row['placementid'],
                    student_id=row['studentid'],
                    selected=row['selected'].lower() == 'true'
                )