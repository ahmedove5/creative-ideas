# Generated by Django 4.0.5 on 2022-06-10 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=128)),
                ('l_name', models.CharField(max_length=128)),
                ('ideas', models.TextField(max_length=256)),
                ('cost', models.IntegerField(max_length=512)),
                ('idea_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=128)),
                ('l_name', models.CharField(max_length=128)),
                ('comments', models.TextField(max_length=512)),
                ('ideas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideas.profile')),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
