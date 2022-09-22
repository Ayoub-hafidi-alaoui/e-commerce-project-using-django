# Generated by Django 3.2 on 2022-09-14 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='products'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='video_url',
            field=models.URLField(blank=True, null=True, verbose_name='video_url'),
        ),
    ]