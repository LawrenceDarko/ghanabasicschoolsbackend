# yourapp/management/commands/import_excel_data.py
import pandas as pd
from django.core.management.base import BaseCommand
from api.models import School

class Command(BaseCommand):
    help = 'Import data from an Excel sheet to the School model'

    def handle(self, *args, **kwargs):

        # df = pd.read_csv('./text.txt', delimiter=None, header=None)
        # self.stdout.write(df)
    # Define the Excel file path
        excel_file_path = 'D:/Developments/Github/SHS profiling project/Backend/shsschools/api/management/commands/shspublicshools.xlsx'

        # Read only the specified columns ('NAME OF SCHOOL', 'DISTRICT', 'LOCATION') from the 'Ashanti' sheet
        columns_to_read = ['NAME OF SCHOOL', 'DISTRICT', 'LOCATION']
        df = pd.read_excel(excel_file_path, sheet_name='WESTERN NORTH', usecols=columns_to_read)
        # self.stdout.write(df.head)

        # Loop through the rows and create/update School objects
        for _, row in df.iterrows():
            name = row['NAME OF SCHOOL']
            district = row['DISTRICT']
            location = row['LOCATION']

            # Check if a School with the same name exists, and update it if needed
            school, created = School.objects.get_or_create(name=name, region='WESTERN NORTH', defaults={'district': district, 'location': location})

            if not created:
                # Update the district and location if the school already existed
                school.district = district
                school.location = location
                school.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
