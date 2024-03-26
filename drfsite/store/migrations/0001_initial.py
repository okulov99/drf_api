# Generated by Django 5.0.3 on 2024-03-26 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название товара')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание товара')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Цена')),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Скидка в %')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
