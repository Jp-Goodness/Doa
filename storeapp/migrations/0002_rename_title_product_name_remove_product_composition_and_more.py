# Generated by Django 4.2.5 on 2023-09-29 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='composition',
        ),
        migrations.AddField(
            model_name='product',
            name='available_quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Available Quantity'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Bags', 'Bags'), ('Beads', 'Beads'), ('Clothes', 'Clothes'), ('Shoes', 'Shoes')], max_length=10),
        ),
    ]