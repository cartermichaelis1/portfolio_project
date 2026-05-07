from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_load_initial_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='image_two',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
