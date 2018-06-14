# Generated by Django 2.0.2 on 2018-06-14 01:09

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
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('usertype_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='account_handling.UserType')),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
            ],
            bases=('account_handling.usertype',),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('usertype_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='account_handling.UserType')),
                ('agent_company', models.CharField(blank=True, max_length=100, null=True)),
            ],
            bases=('account_handling.usertype',),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('usertype_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='account_handling.UserType')),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
            ],
            bases=('account_handling.usertype',),
        ),
        migrations.AddField(
            model_name='usertype',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
