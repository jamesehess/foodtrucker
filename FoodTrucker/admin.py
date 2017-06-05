from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from FoodTrucker.models import FoodTruckType, FoodTruck, VenueType, Venue, Schedule

# Register your models here.
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('foodtruck', 'venue', 'startDateTime', 'endDateTime')

class ScheduleInLine(admin.TabularInline):
    model = Schedule
    extra = 0

class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'url')
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }
    inlines = [ScheduleInLine]

class FoodTruckAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'url')
    fieldsets = [
        (None, {'fields': ['name','type','url','phone_number','description']}),
        ('Update Information', {'fields': ['updateURL','updateNotes']})
    ]
    inlines = [ScheduleInLine]

admin.site.register(FoodTruck, FoodTruckAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(FoodTruckType)
admin.site.register(VenueType)