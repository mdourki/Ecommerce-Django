# Generated by Django 3.2.5 on 2021-07-08 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0004_rename_compte_admi_compte_adm'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_usr', models.CharField(max_length=100)),
                ('prenom_usr', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Compte_adm',
        ),
    ]
