# Generated by Django 4.2.7 on 2025-02-20 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AboutAcademy', '0007_document_title_ar_document_title_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='file_ar',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='document',
            name='file_en',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='document',
            name='file_ky',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='document',
            name='file_ru',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='document',
            name='file_tr',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
    ]
