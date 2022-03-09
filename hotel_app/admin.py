from django.contrib import admin
from .models import (
    Room,
    Category,
    Customer,
    Booking,
    Payment,
    CheckIn,
    CheckOut,
    RoomDisplayImages
)


def change_room_booking_status(model_admin, request, query_set):
    query_set.update(is_booked=False)


change_room_booking_status.short_description_message = "Update all is_booked to False"


class RoomDisplayImagesStacked(admin.StackedInline):
    model = RoomDisplayImages


class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomDisplayImagesStacked]

    class Meta:
        model = Room

    list_display = ['__str__', 'is_booked']
    actions = [change_room_booking_status]


admin.site.register(Room, RoomAdmin)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(CheckIn)
admin.site.register(CheckOut)
admin.site.register(RoomDisplayImages)
