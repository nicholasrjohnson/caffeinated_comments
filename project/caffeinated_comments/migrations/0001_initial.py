# Generated by Django 3.2.7 on 2022-07-03 14:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Comment Date')),
                ('edited_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Edited Date')),
                ('up_vote', models.IntegerField(default=0)),
                ('down_vote', models.IntegerField(default=0)),
                ('post_slug', models.SlugField()),
                ('postid', models.IntegerField(default=0)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='caffeinated_comments.author')),
                ('replied_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='caffeinated_comments.comment')),
            ],
        ),
    ]