from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class report( models.Model):
    user = models.ForeignKey(User, related_name = "agent" , on_delete = models.CASCADE)
    description = models.TextField()
    image = models.ImageField(default = "default.jpg", upload_to = "profile_pics")
    transaction_date = models.DateTimeField(default = timezone.now)
    amount = models.BigIntegerField()
    
    def __str__(self):
        return f"{self.user.username} Profile"
