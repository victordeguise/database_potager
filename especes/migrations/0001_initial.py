# Generated by Django 3.0.6 on 2020-05-14 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Especes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255, unique=True, verbose_name="Nom de l'espèce")),
                ('nom_commun', models.CharField(max_length=255, verbose_name="Nom commun de l'espèce")),
                ('category', models.CharField(blank=True, max_length=255, verbose_name="categorie de l'espèce")),
                ('wiki', models.URLField(blank=True, max_length=255, null=True, verbose_name='lien wikipedia')),
                ('taxonomy', models.IntegerField(blank=True, null=True)),
                ('NCBI', models.CharField(blank=True, max_length=255, null=True, verbose_name="NCBI de l'espèce")),
            ],
            options={
                'verbose_name': 'Espèce',
                'ordering': ['nom'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalEspeces',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('nom', models.CharField(db_index=True, max_length=255, verbose_name="Nom de l'espèce")),
                ('nom_commun', models.CharField(max_length=255, verbose_name="Nom commun de l'espèce")),
                ('category', models.CharField(blank=True, max_length=255, verbose_name="categorie de l'espèce")),
                ('wiki', models.URLField(blank=True, max_length=255, null=True, verbose_name='lien wikipedia')),
                ('taxonomy', models.IntegerField(blank=True, null=True)),
                ('NCBI', models.CharField(blank=True, max_length=255, null=True, verbose_name="NCBI de l'espèce")),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Espèce',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
