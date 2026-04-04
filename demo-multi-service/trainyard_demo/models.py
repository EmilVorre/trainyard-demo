from django.db import models


class DeploymentInfo(models.Model):
    seeded_at = models.DateTimeField(auto_now_add=True)
    framework = models.CharField(max_length=100)
    database = models.CharField(max_length=100)
    note = models.TextField()

    class Meta:
        verbose_name = "Deployment Info"
        verbose_name_plural = "Deployment Info"

    def __str__(self):
        return f"{self.framework} / {self.database}"