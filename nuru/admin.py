from django.contrib import admin

from nuru.models import Information, Notification, Users

# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display= ('full_name','child_name')
    search_fields = ('full_name', 'child_name')

admin.site.register(Users, UsersAdmin)

class InformationAdmin(admin.ModelAdmin):
    list_display= ('neonatal_information','clinical_information')
    search_fields = ('neonatal_information', 'clinical_information')

admin.site.register(Information, InformationAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display= ('message','title','date_time')
    search_fields = ('message','title')

admin.site.register(Notification, NotificationAdmin)
