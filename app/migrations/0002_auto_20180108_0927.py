# Generated by Django 2.0 on 2018-01-08 09:27

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='game',
            managers=[
                ('games', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game',
            name='is_started',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game',
            name='name',
            field=models.TextField(default='UW Weeklong'),
        ),
        migrations.AddField(
            model_name='tag',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tag',
            name='initiator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='initiator_tags', to='app.Player'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_tags', to='app.Player'),
        ),
    ]
