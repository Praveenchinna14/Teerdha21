# Generated by Django 4.2.6 on 2024-04-26 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0027_bus_faq_bus_offercards_bus_trending01_bus_trending1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='bus_special_terms4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(default='', max_length=255)),
                ('point', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='bus_trending2',
            new_name='bus_busday_image6',
        ),
        migrations.RenameModel(
            old_name='bus_trending3',
            new_name='bus_busday_terms6',
        ),
        migrations.RenameModel(
            old_name='bus_trending17',
            new_name='bus_easeday7',
        ),
        migrations.RenameModel(
            old_name='bus_trending19',
            new_name='bus_fest10',
        ),
        migrations.RenameModel(
            old_name='bus_trending7',
            new_name='bus_festival3',
        ),
        migrations.RenameModel(
            old_name='bus_trending4',
            new_name='bus_firstbus_code5',
        ),
        migrations.RenameModel(
            old_name='bus_trending6',
            new_name='bus_firstbus_get5',
        ),
        migrations.RenameModel(
            old_name='bus_trending5',
            new_name='bus_firstbus_terms5',
        ),
        migrations.RenameModel(
            old_name='bus_trending16',
            new_name='bus_go_benefits2',
        ),
        migrations.RenameModel(
            old_name='bus_trending15',
            new_name='bus_go_container2',
        ),
        migrations.RenameModel(
            old_name='bus_trending9',
            new_name='bus_go_image2',
        ),
        migrations.RenameModel(
            old_name='bus_trending8',
            new_name='bus_go_table2',
        ),
        migrations.RenameModel(
            old_name='busfaq',
            new_name='bus_go_terms2',
        ),
        migrations.RenameModel(
            old_name='bus_trending22',
            new_name='bus_holiday12',
        ),
        migrations.RenameModel(
            old_name='bus_trending21',
            new_name='bus_icici11',
        ),
        migrations.RenameModel(
            old_name='bus_trending20',
            new_name='bus_offer9',
        ),
        migrations.RenameModel(
            old_name='bus_trending23',
            new_name='bus_ride13',
        ),
        migrations.RenameModel(
            old_name='Busform',
            new_name='bus_searchform',
        ),
        migrations.RenameModel(
            old_name='bus_trending13',
            new_name='bus_special_avail4',
        ),
        migrations.RenameModel(
            old_name='bus_trending12',
            new_name='bus_special_code4',
        ),
        migrations.RenameModel(
            old_name='bus_trending18',
            new_name='bus_weekday8',
        ),
        migrations.RenameModel(
            old_name='bus_trending1',
            new_name='bus_weekends1',
        ),
        migrations.RenameModel(
            old_name='bus_trending01',
            new_name='bus_weekends_terms1',
        ),
        migrations.DeleteModel(
            name='bus_trending14',
        ),
    ]
