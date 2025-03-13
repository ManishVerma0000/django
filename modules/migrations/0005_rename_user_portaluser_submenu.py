# Generated by Django 5.1.6 on 2025-03-11 18:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0004_alter_menu_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='PortalUser',
        ),
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('path', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='submenuImage/')),
                ('order', models.IntegerField(default=0)),
                ('menuId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submenus', to='modules.menu')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
