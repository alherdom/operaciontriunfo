# Generated by Django 4.2.7 on 2023-12-10 23:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contestant", "0007_alter_contestant_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="contestant",
            name="role",
            field=models.CharField(default="Concursante", max_length=20),
            preserve_default=False,
        ),
    ]
