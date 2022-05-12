# Generated by Django 3.1.2 on 2022-04-14 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('genre', models.PositiveBigIntegerField(choices=[(0, 'Femme'), (1, 'Homme')], null=True)),
                ('age', models.PositiveBigIntegerField(null=True)),
                ('Tension', models.PositiveBigIntegerField(null=True)),
                ('predictions', models.CharField(blank=True, max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]