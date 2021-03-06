# Generated by Django 3.1.7 on 2021-05-24 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planet_alien_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('aliens', models.ManyToManyField(related_name='species', to='planet_alien_app.Alien')),
            ],
        ),
    ]
