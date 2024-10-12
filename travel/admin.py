from django.contrib import admin
from .models import Category, Tour, Hotel, Video

admin.site.register(Category)


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'start_date', 'end_date', 'availability')
    list_filter = ('availability', 'start_date')
    search_fields = ('title', 'location')
    date_hierarchy = 'start_date'


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'rating', 'availability', 'category')
    list_filter = ('category', 'availability', 'rating')
    search_fields = ('title', 'location')
    list_editable = ('availability',)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'tour', 'upload_date')
    list_filter = ('tour',)
    search_fields = ('title',)
