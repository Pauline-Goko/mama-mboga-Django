# Generated by Django 4.2.1 on 2023-06-19 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=16)),
                ('message', models.CharField(max_length=300)),
                ('product_name', models.CharField(max_length=12)),
                ('number_of_stars', models.PositiveIntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]
