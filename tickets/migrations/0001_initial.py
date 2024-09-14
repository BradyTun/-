# Generated by Django 5.0.1 on 2024-09-14 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=96)),
                ('account', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('screenshot', models.ImageField(upload_to='payment_screenshots/')),
                ('ticket_type', models.CharField(choices=[('1', 'Programmer Pass - 15,000 MMK'), ('2', 'Tech Explorer - 30,000  MMK'), ('3', 'Digital Architect - 50,000 MMK'), ('4', 'IT Elite - 100,000 MMK')], max_length=4)),
            ],
        ),
    ]
