# Generated by Django 4.0.3 on 2023-06-28 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id1', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('create_at', models.DateField()),
                ('updated_at', models.DateField()),
            ],
        ),
    ]