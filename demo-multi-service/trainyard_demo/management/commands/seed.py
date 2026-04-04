from django.core.management.base import BaseCommand
from trainyard_demo.models import DeploymentInfo


class Command(BaseCommand):
    help = "Seed initial deployment info record"

    def handle(self, *args, **options):
        if not DeploymentInfo.objects.exists():
            DeploymentInfo.objects.create(
                framework="Django 5.0",
                database="PostgreSQL",
                note="Seeded automatically by migrate job on first deploy.",
            )
            self.stdout.write(self.style.SUCCESS("Seeded DeploymentInfo record"))
        else:
            self.stdout.write("DeploymentInfo already seeded, skipping")