from django.contrib import admin
from app1.models import Employee,Employment

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('Employee_Code', 'Name','photo','Birth_Date','Gender','Age')
    ordering = ('Employee_Code',)
    search_fields = ('Employee_Code', 'Name')
    list_filter = ('Employee_Code', 'Gender')
    #fieldsets = (('Required Information',{'description': "These fields are required for each event.",'fields':(('Employee_Code','Name','Age','Photo'), 'Birth_Date')})

class EmploymentAdmin(admin.ModelAdmin):
    list_display = ('Employee','Confirmation_Date')
    #ordering = ('Employee_Code',)
    #search_fields = ('Employee_Code', 'Name')
    #list_filter = ('Employee_Code', 'Gender')

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Employment,EmploymentAdmin)
