from django.db import models

# Create your models here.

class Sales(models.Model):
    Name = models.CharField(max_length=100)
    Holder = models.CharField(max_length=100)
    ContactNumber = models.CharField(max_length=15, blank=True, null=True)
    Location = models.CharField(max_length=100)
    Assignment = models.CharField(max_length=100)
    Amount = models.FloatField()
    Date = models.DateField(blank=True, null=True)
    DateComplete = models.DateField(blank=True, null=True)  # Allow null values
    AccountNumber = models.CharField(max_length=100, blank=True, null=True)
    Socials = models.JSONField(blank=True, null=True)  # JSONField for handling JSON data
    Status = models.BooleanField(default=False)

    class Meta:
        db_table = 'db_sales'

    
    def __str__(self) -> str:
        return self.Name
    