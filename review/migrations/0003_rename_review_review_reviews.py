# Generated by Django 4.2.6 on 2023-10-26 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_remove_review_user_review_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review',
            new_name='reviews',
        ),
    ]