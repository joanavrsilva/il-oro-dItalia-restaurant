from django.contrib import admin

from .models import Customer
from .models import Reservations

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'phone_number', 'special_requirements', 'updated')
    search_fields = ['name', 'email', 'phone_number']


@admin.register(Reservations)
class ReservationAdmin(admin.ModelAdmin):

    list_display = ('table', 'people', 'reservation_date_time_start', 'reservation_date_time_end', 'created_on')
    list_filter = ('table', 'people', 'reservation_date_time_start', 'reservation_date_time_end', 'created_on')
    search_fields = ('table', 'people', 'reservation_date_time_start', 'reservation_date_time_end', 'created_on')
    actions = ['approve_reservations']

    def approve_reservations(self, request, queryset):
        queryset.update(approved=True)