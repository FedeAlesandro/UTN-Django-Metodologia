from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from rentals.models import Facility, City, Reservation, Estate, RentalDate


class CityAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class FacilityAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class ReservationAdmin(admin.ModelAdmin):
    readonly_fields = ('code', 'amount', 'guest_name', 'guest_last_name', 'guest_email')
    list_display = ("date", "amount", "guest_name")
    list_filter = ("guest_email",)
    search_fields = ("name",)


class EstateAdmin(admin.ModelAdmin):
    list_display = ("title", "pax", "amount")
    list_filter = ("title", "pax",)
    search_fields = ("title",)
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


class RentalDateInline(admin.TabularInline):
    readonly_fields = ('reservation',)
    model = RentalDate
    fk_name = 'estate'
    max_num = 7


class EstateAdmin(admin.ModelAdmin):
    inlines = [RentalDateInline, ]
    list_display = ("title", "pax", "amount")
    list_filter = ("title", "pax",)
    search_fields = ("title",)
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


admin.site.register(Facility, FacilityAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Estate, EstateAdmin)
