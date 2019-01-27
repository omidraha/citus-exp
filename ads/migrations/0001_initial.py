# Generated by Django 2.1.4 on 2019-01-23 14:26

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
            name='Ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=512)),
                ('clicks_count', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=512)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=512)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='campaign',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.Company'),
        ),
        migrations.AddField(
            model_name='ads',
            name='campaign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.Campaign'),
        ),
        migrations.AddField(
            model_name='ads',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.Company'),
        ),
        migrations.AlterUniqueTogether(
            name='campaign',
            unique_together={('id', 'company')},
        ),
        migrations.AlterUniqueTogether(
            name='ads',
            unique_together={('id', 'company')},
        ),
    ]
