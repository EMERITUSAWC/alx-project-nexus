from django.db import models

class Account(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)  # ✅ Added for admin ordering

    def __str__(self):
        return self.username
