# Generated by Django 3.0.8 on 2020-07-20 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0005_upload_reports_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Queries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=50)),
                ('last', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('mobile', models.IntegerField()),
                ('message', models.CharField(max_length=5000)),
            ],
        ),
    ]
