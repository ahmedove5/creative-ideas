# Generated by Django 4.0.4 on 2022-06-12 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ideas', '0003_alter_business_idaea_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oferts', models.BooleanField()),
                ('ideas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideas.business_idaea')),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
