# Generated by Django 5.1.6 on 2025-03-11 17:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0003_remove_menu_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menus', to='modules.user'),
        ),
    ]
