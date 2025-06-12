from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):

    ROLE_CHOICES = [
        ('ngo', 'NGO'),
        ('authority', 'Government Authority'),

    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, null=True, blank=True)
    identification_Number = models.CharField(max_length=12, blank=True, null=True)
    is_individual = models.BooleanField(default=True)

    def _str_(self):
        return f"{self.user.username} - {self.role}"
    

class WasteReport(models.Model):

    WASTE_CATEGORIES = [
        ('kitchen waste', 'Kitchen Waste'),
        ('chemical waste', 'Chemical Waste'),
        ('organic waste', 'Organic Waste'),
        ('recycleable waste', 'Recycleable Waste'),
        ('non-recycleable waste', 'Non-Recycleable Waste'),
        ('construction waste', 'Construction Waste'),
        ('medical waste', 'Medical Waste'),
        ('nuclear waste', 'Nuclear Waste'),

    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=25, choices=WASTE_CATEGORIES)
    title = models.CharField(max_length=50)
    description = models.TextField()
    latitude = models.DecimalField(max_digits=20, decimal_places=16, default= 0.0)
    longitude = models.DecimalField(max_digits=20, decimal_places=16, default= 0.0)
    address = models.CharField(max_length=255)
    submitted_at = models.DateTimeField(auto_now_add = True)

    def _str_(self):
        return f"{self.title or 'Waste Report'} @ {self.address}"
    


class WasteReportImage(models.Model):
    report = models.ForeignKey(WasteReport, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='waste_reports/')

    def __str__(self):
        return f"Image for {self.report.id}"
