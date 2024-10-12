from rest_framework import serializers
from .models import Category, Video, Hotel, Tour


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='travel:category_detail', lookup_field='pk')

    class Meta:
        model = Category
        fields = ['id', 'title', 'url']

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class HotelSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='travel:hotel_detail', lookup_field='pk')
    category = serializers.HyperlinkedRelatedField(view_name='travel:category_detail', queryset=Category.objects.all())

    class Meta:
        model = Hotel
        fields = ['id', 'title', 'description', 'price', 'location', 'rating', 'availability', 'image', 'category', 'url']
        depth = 2

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if not instance.image:
            representation['image'] = self.context['request'].build_absolute_uri('/media/default.jpg')
        representation['image'] = self.context['request'].build_absolute_uri(representation['image'])
        return representation


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
        read_only_fields = ['id', 'upload_date']

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'
        read_only_fields = ['id']

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if not representation['image']:
            representation['image'] = 'media/default.jpg'
        representation['image'] = self.context['request'].build_absolute_uri(representation['image'])
        return representation
