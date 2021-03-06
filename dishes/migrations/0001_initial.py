# Generated by Django 2.0.7 on 2018-07-27 17:08

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('dish_type', models.CharField(choices=[('SOUP', 'Soup'), ('GARNISH', 'Garnish'), ('MEAT', 'Meat'), ('MAIN', 'Main'), ('SALAD', 'Salad')], max_length=7)),
                ('difficulty', models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], default=2)),
                ('seasons', multiselectfield.db.fields.MultiSelectField(choices=[('WINTER', 'Winter'), ('SPRING', 'Spring'), ('SUMMER', 'Summer'), ('AUTUMN', 'Autumn')], max_length=27)),
                ('priority', models.IntegerField(default=100)),
                ('last_used_date', models.DateField(null=True, verbose_name='last use date')),
            ],
        ),
    ]
