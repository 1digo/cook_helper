# Generated by Django 2.0.7 on 2018-07-10 11:32

from django.db import migrations, models


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
                ('dish_type', models.CharField(choices=[('SOUP', 'Soup'), ('GAR', 'Garnish'), ('MEAT', 'Meat'), ('MAIN', 'Main'), ('SAL', 'Salad')], max_length=4)),
                ('season', models.IntegerField(choices=[(0, 'any'), (1, 'winter'), (2, 'spring'), (3, 'summer'), (4, 'autumn')], default=0)),
                ('difficulty', models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], default=2)),
            ],
        ),
    ]