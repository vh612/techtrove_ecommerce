# Generated by Django 5.0.1 on 2024-05-11 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wsite', '0009_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('online', 'direct'), ('direct', 'direct')], max_length=50),
        ),
    ]
