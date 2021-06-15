# Generated by Django 3.2.4 on 2021-06-15 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_alter_employee_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='total_amount_wages',
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_start_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
