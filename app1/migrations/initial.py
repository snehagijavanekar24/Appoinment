import datetime
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
            name='Appointment',
            fields=[
                ('client_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='CLIENT_ID')),
                ('service_id', models.IntegerField()),
                ('scheduled_date', models.DateField(default=datetime.datetime.now)),
                ('status', models.CharField(max_length=100)),
                ('client_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
