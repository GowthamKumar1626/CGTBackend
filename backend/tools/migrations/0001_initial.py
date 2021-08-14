# Generated by Django 3.2.5 on 2021-08-14 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('image', models.FileField(upload_to='images')),
                ('description', models.TextField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Tool',
                'ordering': ('name',),
            },
        ),
    ]
