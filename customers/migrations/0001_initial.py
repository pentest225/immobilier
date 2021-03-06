# Generated by Django 4.0.4 on 2022-05-14 07:12

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
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('dial_code', models.CharField(max_length=4)),
                ('user_image', models.URLField()),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user_type', models.CharField(choices=[('AD', 'ADMIN'), ('AG', 'AGENT'), ('CL', 'CLIENT')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updeted_at', models.DateTimeField(auto_now=True)),
                ('detedt_at', models.DateTimeField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InfoAgent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biographie', models.TextField()),
                ('fb_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('insta_link', models.URLField(blank=True, null=True)),
                ('whatsapp_numero', models.CharField(blank=True, max_length=15, null=True)),
                ('linke_link', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updeted_at', models.DateTimeField(auto_now_add=True)),
                ('detedt_at', models.DateTimeField(null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_info_agent', to='customers.customer')),
            ],
        ),
    ]
