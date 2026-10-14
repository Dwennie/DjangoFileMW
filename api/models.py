from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PortfolioContact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, null=True, blank=True)
    portfolio_url = models.URLField(max_length=200, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject or 'Portfolio Message'}"


class Topic(models.Model):
    CATEGORY_CHOICES = [
        ("Fundamentals", "Fundamentals"),
        ("Web Framework", "Web Framework"),
        ("Database", "Database"),
        ("API", "API"),
        ("Frontend", "Frontend"),
        ("DevOps", "DevOps"),
        ("Other", "Other"),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default="Other")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name