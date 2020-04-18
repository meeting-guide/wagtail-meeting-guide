# Generated by Django 2.2.11 on 2020-03-22 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_guide', '0009_auto_20200321_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='paypal',
            field=models.URLField(blank=True, default='', help_text='Example: https://paypal.me/sepia-mygroup', verbose_name='PayPal URL'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='venmo',
            field=models.URLField(blank=True, default='', help_text='Example: https://venmo.com/sepia-mygroup', verbose_name='Venmo URL'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='video_conference_phone',
            field=models.CharField(blank=True, default='', help_text='Example: 215-555-1212 Code: 123 456 789', max_length=255),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='video_conference_url',
            field=models.URLField(blank=True, default='', help_text='Example: https://zoom.com/j/123456789', verbose_name='Video conference URL'),
        ),
    ]