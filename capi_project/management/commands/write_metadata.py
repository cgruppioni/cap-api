import os
import csv
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    can_import_settings = True

    def handle(self, *args, **options):
        from django.conf import settings
        from capi_project import models

        for root, dirs, files in os.walk(settings.METADATA_DIR_PATH):
            for filename in files:
                try:
                    with open(os.path.join(root, filename), 'rb') as f:
                        reader = csv.DictReader(f)
                        for i,row in enumerate(reader):
                            try:
                                models.Case.create_from_row(row)

                            except Exception as e:
                                self.stdout.write("Error in row %s: %s %s %s" % (os.path.join(root, filename), e,i,row)))
                                pass
                    self.stdout.write(self.style.SUCCESS("Success %s" % os.path.join(root, filename)))
                    # move file to archive directory
                    os.rename(os.path.join(root, filename), os.path.join(settings.METADATA_ARCHIVE_DIR_PATH, filename))
                except Exception as e:
                    self.stdout.write("Error in file: %s" % os.path.join(root, filename)))
