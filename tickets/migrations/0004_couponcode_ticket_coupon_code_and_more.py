# Generated by Django 5.0.1 on 2024-09-24 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_ticket_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CouponCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('ticket_type', models.CharField(choices=[('1', 'Programmer Pass - 15,000 MMK'), ('2', 'Tech Explorer - 30,000  MMK'), ('3', 'Digital Architect - 50,000 MMK'), ('4', 'IT Elite - 100,000 MMK')], max_length=4)),
                ('is_redeemed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='ticket',
            name='coupon_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='screenshot',
            field=models.ImageField(blank=True, null=True, upload_to='payment_screenshots/'),
        ),
    ]
