# Generated by Django 3.2 on 2021-06-21 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approve_comment',
            field=models.BooleanField(default=False),
        ),
    ]
