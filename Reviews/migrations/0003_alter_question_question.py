# Generated by Django 4.1.7 on 2023-06-12 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0002_rename_ans_answer_answer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(),
        ),
    ]
