# Generated by Django 2.2 on 2019-07-19 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productcourse', '0017_product_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_logo',
            field=models.ImageField(blank=True, null=True, upload_to='courses/'),
        ),
    ]
