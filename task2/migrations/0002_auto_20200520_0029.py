# Generated by Django 3.0.6 on 2020-05-19 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='SOME STRING', max_length=100)),
                ('text', models.TextField()),
                ('timeallow', models.DateTimeField(auto_now_add=True)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
