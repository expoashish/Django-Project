# Generated by Django 3.1.4 on 2021-01-07 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_book', '0005_auto_20210107_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_details',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
