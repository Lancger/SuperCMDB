# Generated by Django 2.1.3 on 2018-12-04 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20181204_0738'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='log',
            options={'verbose_name': '登录日志', 'verbose_name_plural': '登录日志'},
        ),
        migrations.AlterModelOptions(
            name='ttylog',
            options={'verbose_name': '操作日志', 'verbose_name_plural': '操作日志'},
        ),
        migrations.AlterField(
            model_name='log',
            name='host',
            field=models.CharField(max_length=128, null=True, verbose_name='登录主机'),
        ),
    ]
