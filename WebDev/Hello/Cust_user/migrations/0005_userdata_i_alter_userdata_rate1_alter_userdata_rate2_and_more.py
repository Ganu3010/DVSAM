# Generated by Django 4.0.4 on 2022-05-17 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cust_user', '0004_remove_userdata_i_alter_userdata_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='i',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='rate1',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='rate2',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='rate3',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='rate4',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='rate5',
            field=models.IntegerField(default=-1),
        ),
    ]
