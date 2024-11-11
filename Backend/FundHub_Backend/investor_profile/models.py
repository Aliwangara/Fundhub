from django.db import models
from startup_profile.models import industry, startup_profile
# Create your models here.


# Investors data
class investor_profile(models.Model):
    name = models.CharField(max_length=20)
    profile_pic = models.ImageField(upload_to='investor_profile/images/')
    Bio = models.CharField(max_length=500)
    investment_preferences = models.ManyToManyField(industry)
    funding_range_min = models.DecimalField(max_digits=10, decimal_places=2)
    funding_range_max = models.DecimalField(max_digits=10, decimal_places=2)
    portfolio_companies = models.CharField(blank=True,null=True, max_length=400)

class Conversation(models.Model):
    investor = models.ForeignKey('investor_profile', on_delete=models.CASCADE)
    startup = models.ForeignKey(startup_profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(investor_profile, null=True, blank=True, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(startup_profile, null=True, blank=True, on_delete=models.CASCADE, related_name='received_messages')
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


 