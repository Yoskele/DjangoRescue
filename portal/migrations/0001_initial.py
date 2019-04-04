# Generated by Django 2.2 on 2019-04-03 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('location', models.CharField(max_length=200)),
                ('severity', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High'), ('critical', 'Critical')], default='medium', max_length=10)),
                ('category', models.CharField(choices=[('fire', 'Fire'), ('earth', 'Earth'), ('water', 'Water'), ('storm', 'Storm'), ('disease', 'Disease'), ('industrial', 'Industrial')], default='fire', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PersonStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
