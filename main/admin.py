from django.contrib import admin

from .models import Hotel, Region, Rating, Room, RoomType, RoomRating


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    pass


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['hotel', 'room_type', 'rate', 'name', 'price']
    list_editable = ['rate', 'price']
    list_filter = ['hotel']
    search_fields = ['hotel', 'name', 'id']


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(RoomRating)
class RoomRatingAdmin(admin.ModelAdmin):
    pass
