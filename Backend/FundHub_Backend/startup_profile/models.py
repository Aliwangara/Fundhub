from django.db import models
# from investor_profile.models import investor_profile
from django.core.exceptions import ValidationError
# Create your models here.

# Type of industry whether tech or health etc
class industry(models.Model):
    Name = models.CharField(max_length=10)


# stage of development (entry, mid )
class stage(models.Model):
    Name = models.CharField(max_length=10)

def validate_file_size(value):
    limit = 5 * 1024 * 1024  # 5 MB limit
    if value.size > limit:
        raise ValidationError('File size must be under 5 MB.')

# Companies profile
class startup_profile(models.Model):
    Business_name = models.CharField(null=False, max_length=100)
    Logo = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500)
    funding_needs = models.DecimalField(max_digits=10, decimal_places=2)
    equity_offered = models.FloatField()
    industry = models.ForeignKey(industry, on_delete=models.CASCADE)
    stage = models.ForeignKey(stage, on_delete=models.CASCADE)

    pitch_deck = models.FileField(upload_to='documents/', validators=[validate_file_size])

# Reviews of investor and company interaction
class startup_reviews(models.Model):
    investor = models.ForeignKey('investor_profile.investor_profile', on_delete=models.CASCADE)
    startup = models.ForeignKey(startup_profile, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)




