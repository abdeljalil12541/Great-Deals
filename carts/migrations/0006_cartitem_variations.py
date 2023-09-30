# Generated by Django 4.2.5 on 2023-09-28 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_product_id_alter_variation_id'),
        ('carts', '0005_remove_cartitem_variations'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.variation'),
        ),
    ]
