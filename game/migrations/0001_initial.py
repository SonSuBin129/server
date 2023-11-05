# Generated by Django 4.2.7 on 2023-11-05 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=64)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'games',
            },
        ),
        migrations.CreateModel(
            name='TrashCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=512)),
            ],
            options={
                'db_table': 'trash_category',
            },
        ),
        migrations.CreateModel(
            name='Trash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=512)),
                ('image_url', models.CharField(max_length=512)),
                ('difficulty', models.IntegerField()),
                ('trash_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.trashcategory')),
            ],
            options={
                'db_table': 'trashes',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_answer', models.BooleanField(null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.game')),
                ('trash', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.trash')),
            ],
            options={
                'db_table': 'records',
            },
        ),
    ]
