# Generated by Django 3.2.10 on 2023-07-23 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComplaintMS', '0002_alter_profile_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Branch',
            field=models.CharField(choices=[('Bhopal', 'Bhopal'), ('Kothri', 'Kothri'), ('Indore', 'Indore'), ('Aashta', 'Aashta'), ('Dewas', 'Dewas')], default='Kothri', max_length=29),
        ),
        migrations.AlterField(
            model_name='profile',
            name='collegename',
            field=models.CharField(choices=[('Garbage Removal', 'Garbage Removal'), ('Garbage Pickup', 'Garbage Pickup')], max_length=29),
        ),
    ]
