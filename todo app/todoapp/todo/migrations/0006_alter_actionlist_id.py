# Generated by Django 5.0.7 on 2024-07-24 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_alter_actionlist_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionlist',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
