from django.db import models

class MessageLog(models.Model):
    message = models.TextField()
    predictions = models.JSONField()  # Works with SQLite, no PostgreSQL needed
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.message[:30]}... at {self.created_at}"
