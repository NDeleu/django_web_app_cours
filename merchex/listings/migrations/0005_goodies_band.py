# Generated by Django 4.2.1 on 2023-05-29 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_goodies_description_goodies_sold_goodies_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodies',
            name='band',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.band'),
        ),
    ]
