# Generated by Django 3.0.8 on 2020-12-20 20:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_auto_20201213_1847'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogComments',
            new_name='BlogComment',
        ),
        migrations.AlterField(
            model_name='blogimage',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
