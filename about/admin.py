# about/admin.py

from django.contrib import admin
from .models import about

'''class AboutAdmin(admin.ModelAdmin):
    change_form_template = 'admin/about_about_change_form.html'

admin.site.register(about, AboutAdmin)'''

@admin.register(about)
class AboutAdmin(admin.ModelAdmin):
    change_list_template = 'admin/about_change_list.html'
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request):
        return False