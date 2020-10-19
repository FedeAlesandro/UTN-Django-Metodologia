from django.contrib import admin
from rentals.models import Facility, City, Reservation, Estate, RentalDate


class CityAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class FacilityAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class ReservationAdmin(admin.ModelAdmin):
    list_display = ("since_date", "to_date", "amount", "guest_name")
    list_filter = ("guest_email",)
    search_fields = ("name",)


class RentalDateAdmin(admin.ModelAdmin):
    list_display = ("estate",
                    "date",)
    list_filter = ("date",)
    date_hierarchy = "date"


class EstateAdmin(admin.ModelAdmin):
    list_display = ("title", "pax", "amount")
    list_filter = ("title", "pax",)
    search_fields = ("title",)


admin.site.register(Facility, FacilityAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(RentalDate, RentalDateAdmin)
admin.site.register(Estate, EstateAdmin)
