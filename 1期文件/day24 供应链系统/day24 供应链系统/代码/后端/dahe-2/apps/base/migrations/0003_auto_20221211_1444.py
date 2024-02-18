# Generated by Django 3.2 on 2022-12-11 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_company_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyauth',
            name='leader_identity_back',
            field=models.CharField(default=1, max_length=128, verbose_name='身份证-国徽'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='companyauth',
            name='leader_identity_front',
            field=models.CharField(default=1, max_length=128, verbose_name='身份证-人头'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='companyauth',
            name='licence_path',
            field=models.CharField(max_length=128, verbose_name='营业执照'),
        ),
    ]
