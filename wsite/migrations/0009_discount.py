# Generated by Django 5.0.1 on 2024-05-08 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wsite', '0008_payment_vnpay'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=200, null=True)),
                ('discount_value', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
