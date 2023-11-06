from django.contrib import admin

from main_app.models import Employee


# Register your models here.

admin.site.site_header = "Mtoni Application"
admin.site.index_title = "Mtoni"
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "dob", "disabled"]
    search_fields = ["name", "email"]
    list_filter = ["disabled"]


admin.site.register(Employee, EmployeeAdmin)
