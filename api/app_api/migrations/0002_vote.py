# Generated by Django 4.2.5 on 2023-09-26 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_api.employee')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_api.menu')),
            ],
        ),
    ]
