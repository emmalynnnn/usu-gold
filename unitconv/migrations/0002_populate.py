# Generated by Django 4.1.6 on 2023-03-27 00:58

from django.db import migrations


def populate_db(apps, schema_editor):
    ConversionFactor = apps.get_model('unitconv', 'ConversionFactor')

    T = ConversionFactor(name="T", to_troy_oz=32150)
    T.save()
    g = ConversionFactor(name="g", to_troy_oz=.0321507)
    g.save()
    t_oz = ConversionFactor(name="t_oz", to_troy_oz=1)
    t_oz.save()
    kg = ConversionFactor(name="kg", to_troy_oz=32.1507)
    kg.save()
    lb = ConversionFactor(name="lb", to_troy_oz=14.5833)
    lb.save()
    oz = ConversionFactor(name="oz", to_troy_oz=.911458)
    oz.save()


class Migration(migrations.Migration):

    dependencies = [
        ('unitconv', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_db)
    ]
