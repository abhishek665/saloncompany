# Generated by Django 4.2 on 2023-05-02 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sc', '0003_services_uid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='price',
            new_name='uid',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='benefits',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='brand_products',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='face_type',
        ),
        migrations.CreateModel(
            name='AtomCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('benefits', models.CharField(blank=True, max_length=255, null=True)),
                ('face_type', models.CharField(blank=True, choices=[('Dry Skin', 'Dry Skin'), ('Oily Skin', 'Oily Skin'), ('All Types', 'All Types')], max_length=255, null=True)),
                ('discount', models.CharField(blank=True, max_length=255, null=True)),
                ('brand_products', models.CharField(blank=True, choices=[('Loreal', 'Loreal'), ('Pearls', 'Pearls'), ('Nivia', 'Nivia')], max_length=255, null=True)),
                ('atom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sc.subcategory')),
            ],
        ),
    ]