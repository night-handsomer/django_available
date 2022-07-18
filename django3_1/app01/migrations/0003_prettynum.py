# Generated by Django 3.2.7 on 2022-01-15 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20220116_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrettyNum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=32, verbose_name='手机号')),
                ('price', models.IntegerField(default=0, verbose_name='价格')),
                ('level', models.SmallIntegerField(choices=[(1, '1级'), (2, '2级'), (3, '3级'), (4, '4级')], default=1, verbose_name='级别')),
                ('status', models.SmallIntegerField(choices=[(1, '未占用'), (2, '已占用')], default=2, verbose_name='占用状态')),
            ],
        ),
    ]
