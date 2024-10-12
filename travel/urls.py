from django.urls import path
from . import views

app_name = 'travel'
urlpatterns = [
    path('category/list/', views.CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/detail/', views.CategoryDetailView.as_view(), name='category_detail'),

    path('video/list/', views.VideoListView.as_view(), name='video_list'),
    path('video/<int:pk>/detail/', views.VideoDetailView.as_view(), name='video_detail'),

    path('hotel/list/', views.HotelListView.as_view(), name='hotel_list'),
    path('hotel/<int:pk>/detail/', views.HotelDetailView.as_view(), name='hotel_detail'),

    path('tour/list/', views.TourListView.as_view(), name='tour_list'),
    path('tour/<int:pk>/detail/', views.TourDetailView.as_view(), name='tour_detail'),
]
