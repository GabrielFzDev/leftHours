# Generated by Django 4.2.2 on 2023-06-12 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameAction', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameCategory', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('projectBegin', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('responsible', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workedHours', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField()),
                ('initialDate', models.DateField()),
                ('terminalDate', models.DateField()),
                ('snapshot', models.DateTimeField(auto_now=True)),
                ('action', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.action')),
                ('categoryAction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.categoryaction')),
                ('idproject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.projects')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='action',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.categoryaction'),
        ),
    ]
