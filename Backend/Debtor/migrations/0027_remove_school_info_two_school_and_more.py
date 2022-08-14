# Generated by Django 4.0.5 on 2022-08-13 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Debtor', '0026_remove_school_founded_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school_info_two',
            name='school',
        ),
        migrations.RemoveField(
            model_name='school_owner_info',
            name='school',
        ),
        migrations.AddField(
            model_name='school',
            name='Founded',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='Number_of_students',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='Number_of_teachers',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='Permanent_address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='Phone_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='Reg_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='Registered_session',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='School_owner',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='Session',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='current_address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='School_info_one',
        ),
        migrations.DeleteModel(
            name='School_info_two',
        ),
        migrations.DeleteModel(
            name='School_owner_info',
        ),
    ]