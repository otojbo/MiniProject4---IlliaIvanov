# INF 601 - Advanced Python
# Illia Ivanov
# Mini Project 4

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class DailyEntry(models.Model):
    # Mood choices
    MOOD_CHOICES = [
        ('happy', '😊 Happy'),
        ('neutral', '😐 Neutral'),
        ('sad', '😢 Sad'),
        ('angry', '😤 Angry'),
        ('tired', '😴 Tired'),
    ]

    # Basic fields
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries')
    date = models.DateField()
    title = models.CharField(max_length=200)
    content = models.TextField(help_text="Write about your day...")
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES, default='neutral')

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Daily Entries"
        ordering = ['-date']
        unique_together = ['user', 'date']

    def __str__(self):
        return f"{self.date} - {self.title}"

    def get_absolute_url(self):
        return reverse('journal:entry_detail', kwargs={'pk': self.pk})


class DailyTask(models.Model):
    # Priority choices
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    # Basic fields
    daily_entry = models.ForeignKey(DailyEntry, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-priority', 'completed']

    def __str__(self):
        status = "✓" if self.completed else "○"
        return f"{status} {self.title}"