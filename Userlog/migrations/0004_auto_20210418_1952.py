# Generated by Django 3.1.7 on 2021-04-19 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Userlog', '0003_auto_20210330_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='cust_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='entries', to='Userlog.customer'),
        ),
    ]
