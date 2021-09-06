# Generated by Django 3.2.6 on 2021-09-06 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SerializerTry', '0004_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='SerializerTry.person')),
                ('subject', models.CharField(default='', max_length=10)),
            ],
            bases=('SerializerTry.person',),
        ),
    ]
