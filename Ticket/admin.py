from django.contrib import admin
from .models import Ticket


class TicketAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.save(request=request)  # Pass request to the save method of the model
        
    list_display = ('title', 'Author', 'assigned_to','priority', 'Is_It_a_Problem', 'created_at', 'solved', 'Date', 'Time', 'Provide_Email', 'Provide_URL')
    list_filter = ( 'solved','Author','assigned_to', 'Is_It_a_Problem','priority', 'created_at', 'Any_Value', 'Date', 'Provide_Email', 'Provide_URL')
    search_fields = ['title', 'Provide_Email', 'Provide_URL', 'Author__username', 'assigned_to__username']
    list_per_page = 10
    list_editable = ('Is_It_a_Problem','assigned_to','priority','solved')

    # Function to return the full name of the assigned user
    def get_assigned_to_full_name(self, obj):
        return obj.assigned_to.get_full_name() if obj.assigned_to else ''


admin.site.register(Ticket, TicketAdmin)