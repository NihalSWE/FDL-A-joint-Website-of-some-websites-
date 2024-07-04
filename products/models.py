from django.db import models

class Portfolio(models.Model):
    file = models.FileField(upload_to='portfolios/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Portfolio uploaded on {self.id}"
