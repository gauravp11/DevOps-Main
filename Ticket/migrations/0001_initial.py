# Generated by Django 5.0.2 on 2024-03-07 10:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('Is_It_a_Problem', models.BooleanField(choices=[(True, 'Yes'), (False, 'No'), (False, 'Maybe')], default=False, help_text="Check this if it's a problem and needed Solution")),
                ('solved', models.CharField(choices=[('Yes', 'Open'), ('No', 'Closed')], default='Yes', max_length=3, verbose_name='Solved')),
                ('priority', models.CharField(blank=True, choices=[('Low', 'Low'), ('Normal', 'Normal'), ('High', 'High'), ('Critical', 'Critical')], max_length=10, null=True, verbose_name='Priority')),
                ('content', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='note_attachments/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='note_images/')),
                ('Any_Value', models.IntegerField(blank=True, null=True)),
                ('Date', models.DateField(blank=True, null=True)),
                ('Time', models.TimeField(blank=True, null=True)),
                ('Provide_Email', models.EmailField(blank=True, max_length=254, null=True)),
                ('Provide_URL', models.URLField(blank=True, null=True)),
                ('Author', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authored_notes', to=settings.AUTH_USER_MODEL, verbose_name='Author / Reporter')),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_notes', to=settings.AUTH_USER_MODEL, verbose_name='Assigned To')),
            ],
            options={
                'verbose_name': 'Internal Ticket',
                'verbose_name_plural': 'Internal Tickets',
            },
        ),
    ]