from django.db import migrations
from django.core.management import call_command


def load_fixture(apps, schema_editor):
    call_command('loaddata', 'initial_data', app_label='core')


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_project_image_two'),
    ]

    operations = [
        migrations.RunPython(load_fixture, migrations.RunPython.noop),
    ]
