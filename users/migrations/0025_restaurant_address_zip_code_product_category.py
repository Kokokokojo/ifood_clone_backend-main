# Generated by Django 4.2.1 on 2024-03-13 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_alter_customuser_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('description', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='logos/')),
                ('street', models.CharField(max_length=75)),
                ('neighborhood', models.CharField(max_length=75)),
                ('number', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=75)),
                ('state', models.CharField(max_length=75)),
                ('zip_code', models.CharField(max_length=8)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='zip_code',
            field=models.CharField(default=1, max_length=8),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('description', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='logos/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('qtd', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('description', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.product')),
            ],
        ),
    ]
