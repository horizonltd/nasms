# Generated by Django 2.1.4 on 2019-02-19 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='Address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='Doctor_Name',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='Sex',
            field=models.CharField(default='', max_length=7),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='Specialization',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Age',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Phone_Number',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]
