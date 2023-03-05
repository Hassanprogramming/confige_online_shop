# Generated by Django 4.1.7 on 2023-03-02 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('digital', models.BooleanField(default=False, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(max_length=500, null=True)),
                ('luxury', models.BooleanField(default=False, null=True)),
            ],
        ),
    ]