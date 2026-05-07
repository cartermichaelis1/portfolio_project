from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('ml', 'Machine Learning'),
        ('nlp', 'NLP'),
        ('cv', 'Computer Vision'),
        ('da', 'Data Analysis'),
        ('web', 'Web Development'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    summary = models.TextField()
    business_problem = models.TextField()
    tools_used = models.CharField(max_length=500)
    key_features = models.TextField()
    role_contribution = models.TextField()
    biggest_challenge = models.TextField()
    lessons_learned = models.TextField()
    image = models.CharField(max_length=200, blank=True)
    image_two = models.CharField(max_length=200, blank=True)
    github_link = models.URLField(blank=True)
    demo_link = models.URLField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('programming', 'Programming & Data'),
        ('ai_tools', 'AI Tools'),
        ('marketing', 'Marketing & Advertising'),
        ('analytics', 'Analytics & Platforms'),
        ('other_tools', 'Other Tools'),
    ]

    PROFICIENCY_CHOICES = [
        (1, 'Beginner'),
        (2, 'Elementary'),
        (3, 'Intermediate'),
        (4, 'Advanced'),
        (5, 'Expert'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    proficiency = models.IntegerField(choices=PROFICIENCY_CHOICES, default=3)

    def __str__(self):
        return f"{self.name} ({self.get_proficiency_display()})"

    class Meta:
        ordering = ['category', '-proficiency']


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.subject}"

    class Meta:
        ordering = ['-submitted_at']
