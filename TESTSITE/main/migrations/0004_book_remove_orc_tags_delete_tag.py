# Generated by Django 4.1.3 on 2023-02-07 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_tag_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('content', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Книги',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.RemoveField(
            model_name='orc',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
