# Generated by Django 4.1.7 on 2023-03-03 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True)),
                ('price', models.FloatField()),
                ('digital', models.BooleanField(default=False, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(max_length=500, null=True)),
                ('luxury', models.BooleanField(default=False, null=True)),
                ('luxury_1', models.BooleanField(default=False, null=True)),
                ('luxury_2', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Website_Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_title', models.CharField(max_length=150, null=True)),
                ('title', models.CharField(max_length=250, null=True)),
                ('text', models.TextField(max_length=300, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.admin')),
            ],
        ),
    ]