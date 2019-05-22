# Generated by Django 2.2 on 2019-05-22 14:44

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
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=150)),
                ('story', models.TextField()),
                ('date', models.DateField()),
                ('like', models.IntegerField()),
                ('genre', models.CharField(choices=[('0', 'Horror'), ('1', 'Romantic'), ('2', 'SCI-FI')], max_length=1)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=75)),
                ('statusid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.Status')),
            ],
        ),
    ]