# Generated by Django 4.2.2 on 2023-06-11 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_post_category_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='Ernest', max_length=30),
        ),
    ]
