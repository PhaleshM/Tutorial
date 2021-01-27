# Generated by Django 3.1.4 on 2020-12-15 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180, unique=True)),
                ('author', models.CharField(max_length=64)),
                ('disciption', models.TextField(null=True, unique=True)),
                ('youtube_vid', models.CharField(max_length=11)),
                ('star_count', models.DecimalField(decimal_places=1, max_digits=2)),
                ('category', models.IntegerField(choices=[(1, 'HTML/CSS'), (2, 'JAVASCRIPT'), (3, 'PYTHON'), (4, 'DJANGO')])),
                ('skill_level', models.IntegerField(choices=[(1, 'BEGINNER'), (2, 'INTERMEDIATE'), (3, 'EXPERT')])),
                ('is_active', models.BooleanField(default=True)),
                ('posted_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-star_count', 'title'],
            },
        ),
    ]
