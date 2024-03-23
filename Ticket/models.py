from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Ticket(models.Model):

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Normal', 'Normal'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    ]

    SOLVED_CHOICES = [
        ('Yes', 'Open'),
        ('No', 'Closed'),
    ]


    title = models.CharField(max_length=100, verbose_name='Title')
    Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, editable=False, verbose_name='Author / Reporter', related_name='authored_notes')
    
    Is_It_a_Problem = models.BooleanField(default=False,
                            help_text="Check this if it's a problem and needed Solution",
                            choices=[(True, 'Yes'), (False, 'No'), (False,'Maybe')])
    
    solved = models.CharField(max_length=3, choices=SOLVED_CHOICES, default='Yes', verbose_name='Solved')

    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, null=True, blank=True, verbose_name='Priority')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Assigned To', related_name='assigned_notes')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(upload_to='note_attachments/', null=True, blank=True)
    image = models.ImageField(upload_to='note_images/', null=True, blank=True)
    Any_Value = models.IntegerField(null=True, blank=True)
    Date = models.DateField(null=True, blank=True)
    Time = models.TimeField(null=True, blank=True)
    Provide_Email = models.EmailField(max_length=254, null=True, blank=True)
    Provide_URL = models.URLField(max_length=200, null=True, blank=True)

    def clean(self):
        super().clean()
        # Check if Is_It_a_Problem is True and assigned_to or priority is not set
        if self.Is_It_a_Problem and (not self.assigned_to or not self.priority):
            raise ValidationError("Assigned to and Priority cannot be empty if Is It a Problem is selected as Yes.")
        
    def save(self, *args, **kwargs):
        # Retrieve and remove the request from kwargs if present
        request = kwargs.pop('request', None)
        
        # Set author to the currently logged-in user if it's not set
        if not self.Author and request:
            self.Author = request.user
        
        # Call the save method of the parent class
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Internal Ticket"
        verbose_name_plural = "Internal Tickets"