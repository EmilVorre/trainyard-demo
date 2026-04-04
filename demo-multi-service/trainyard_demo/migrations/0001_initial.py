from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DeploymentInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("seeded_at", models.DateTimeField(auto_now_add=True)),
                ("framework", models.CharField(max_length=100)),
                ("database", models.CharField(max_length=100)),
                ("note", models.TextField()),
            ],
            options={
                "verbose_name": "Deployment Info",
                "verbose_name_plural": "Deployment Info",
            },
        ),
    ]