from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CategorySerializer, VideoSerializer, HotelSerializer, TourSerializer
from .models import Category, Video, Hotel, Tour


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'message': 'Kategoriya qo\'shildi', 'data': serializer.data})
        return Response(serializer.errors, status=400)


class CategoryDetailView(APIView):
    def get(self, request, pk):
        try:
            category = Category.objects.get(id=pk)
            serializer = CategorySerializer(category, context={'request': request})
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response({'message': 'Kategoriya topilmadi'}, status=404)

    def put(self, request, pk):
        try:
            category = Category.objects.get(id=pk)
            serializer = CategorySerializer(category, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'message': 'Ma\'lumot yangilandi', 'data': serializer.data})
            return Response(serializer.errors, status=400)
        except Category.DoesNotExist:
            return Response({'status': 'error', 'message': 'Ma\'lumot topilmadi'}, status=404)

    def patch(self, request, pk):
        try:
            category = Category.objects.get(id=pk)
            serializer = CategorySerializer(category, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'message': 'Ma\'lumot qisman yangilandi', 'data': serializer.data})
            return Response(serializer.errors, status=400)
        except Category.DoesNotExist:
            return Response({'status': 'error', 'message': 'Ma\'lumot topilmadi'}, status=404)

    def delete(self, request, pk):
        try:
            category = Category.objects.get(id=pk)
            category.delete()
            return Response({'status': 'success', 'message': 'Kategoriya o\'chirildi'})
        except Category.DoesNotExist:
            return Response({'status': 'error', 'message': 'Kategoriya topilmadi'}, status=404)


class VideoListView(APIView):
    def get(self, request):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'message': 'Video qo\'shildi', 'data': serializer.data})
        return Response(serializer.errors, status=400)


class VideoDetailView(APIView):
    def get(self, request, pk):
        try:
            video = Video.objects.get(id=pk)
            serializer = VideoSerializer(video)
            return Response(serializer.data)
        except Video.DoesNotExist:
            return Response({'message': 'Video topilmadi'}, status=404)

    def put(self, request, pk):
        try:
            video = Video.objects.get(id=pk)
            serializer = VideoSerializer(video, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'message': 'Ma\'lumot yangilandi', 'data': serializer.data})
            return Response(serializer.errors, status=400)
        except Video.DoesNotExist:
            return Response({'status': 'error', 'message': 'Ma\'lumot topilmadi'}, status=404)

    def patch(self, request, pk):
        try:
            video = Video.objects.get(id=pk)
            serializer = VideoSerializer(video, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'message': 'Ma\'lumot qisman yangilandi', 'data': serializer.data})
            return Response(serializer.errors, status=400)
        except Video.DoesNotExist:
            return Response({'status': 'error', 'message': 'Video topilmadi'}, status=404)

    def delete(self, request, pk):
        try:
            video = Video.objects.get(id=pk)
            video.delete()
            return Response({'status': 'success', 'message': 'Video o\'chirildi'})
        except Video.DoesNotExist:
            return Response({'status': 'error', 'message': 'Video topilmadi'}, status=404)


class HotelListView(APIView):
    def get(self, request):
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        serializer = HotelSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'message': 'Ma\'lumot qo\'shildi', 'data': serializer.data})
        return Response(serializer.errors, status=400)


class HotelDetailView(APIView):
    def get(self, request, pk):
        try:
            hotel = Hotel.objects.get(id=pk)
            serializer = HotelSerializer(hotel, context={"request": request})
            return Response(serializer.data)
        except Hotel.DoesNotExist:
            return Response({'message': 'Ma\'lumot topilmadi'}, status=404)

    def put(self, request, pk):
        try:
            hotel = Hotel.objects.get(id=pk)
            serializer = HotelSerializer(hotel, data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'message': 'Ma\'lumot yangilandi', 'data': serializer.data})
            return Response(serializer.errors, status=400)
        except Hotel.DoesNotExist:
            return Response({'status': 'error', 'message': 'Ma\'lumot topilmadi'}, status=404)

    def patch(self, request, pk):
        try:
            hotel = Hotel.objects.get(id=pk)
            serializer = HotelSerializer(hotel, data=request.data, partial=True, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'message': 'Ma\'lumot qisman yangilandi', 'data': serializer.data})
            return Response(serializer.errors, status=400)
        except Hotel.DoesNotExist:
            return Response({'status': 'error', 'message': 'Ma\'lumot topilmadi'}, status=404)

    def delete(self, request, pk):
        try:
            hotel = Hotel.objects.get(id=pk)
            hotel.delete()
            return Response({'status': 'success', 'message': 'Ma\'lumot o\'chirildi'})
        except Hotel.DoesNotExist:
            return Response({'status': 'error', 'message': 'Ma\'lumot topilmadi'}, status=404)


class TourListView(APIView):
    def get(self, request):
        tours = Tour.objects.all()
        serializer = TourSerializer(tours, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        serializer = TourSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'message': 'Ma\'lumot qo\'shildi', 'data': serializer.data})
        return Response(serializer.errors, status=400)


class TourDetailView(APIView):
    def get(self, request, pk):
        try:
            tour = Tour.objects.get(id=pk)
            serializer = TourSerializer(tour, context={"request": request})
            return Response(serializer.data)
        except Tour.DoesNotExist:
            return Response({'message': 'Ma\'lumot topilmadi'}, status=404)

    def put(self, request, pk):
        try:
            tour = Tour.objects.get(id=pk)
            serializer = TourSerializer(tour, data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'message': 'Ma\'lumot yangilandi', 'data': serializer.data})
            return Response(serializer.errors, status=400)
        except Tour.DoesNotExist:
            return Response({'status': 'error', 'message': 'Ma\'lumot topilmadi'}, status=404)

    def patch(self, request, pk):
        try:
            tour = Tour.objects.get(id=pk)
            serializer = TourSerializer(tour, data=request.data, partial=True, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'message': 'Ma\'lumot qisman yangilandi', 'data': serializer.data})
            return Response(serializer.errors, status=400)
        except Tour.DoesNotExist:
            return Response({'status': 'error', 'message': 'Ma\'lumot topilmadi'}, status=404)

    def delete(self, request, pk):
        try:
            tour = Tour.objects.get(id=pk, context={"request": request})
            tour.delete()
            return Response({'status': 'success', 'message': 'Ma\'lumot o\'chirildi'})
        except Tour.DoesNotExist:
            return Response({'status': 'error', 'message': 'Ma\'lumot topilmadi'}, status=404)
