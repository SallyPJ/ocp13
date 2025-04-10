# Generated by Django 3.0 on 2025-03-17 17:03

from django.db import migrations

def copy_letting_data(apps, schema_editor):
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')

    Address = apps.get_model('letting', 'Address')
    Letting = apps.get_model('letting', 'Letting')

    for old_address in OldAddress.objects.all():
        new_address = Address.objects.create(
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code,
        )

    for old_letting in OldLetting.objects.all():
        Letting.objects.create(
            title=old_letting.title,
            address=Address.objects.get(id=old_letting.address.id),
        )

class Migration(migrations.Migration):

    dependencies = [
        ('letting', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(copy_letting_data),
    ]
