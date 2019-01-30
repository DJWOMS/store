from rest_framework import serializers
from photologue.models import Gallery, Photo

from .models import Product


class PhotoSer(serializers.ModelSerializer):
    """Изображений"""
    class Meta:
        model = Photo
        fields = ("image",)


class GallerySer(serializers.ModelSerializer):
    """Галерея"""
    photos = PhotoSer()
    class Meta:
        model = Gallery
        fields = ("galleries",)


class ProductSer(serializers.ModelSerializer):
    """Сериализация продуктов"""
    # gallery = GallerySer()
    # photo = PhotoSer()
    class Meta:
        model = Product
        fields = (
            "category",
            "title",
            "description",
            "price",
            "slug",
            "availability",
            "quantity",
            "photo",
            "gallery",
        )