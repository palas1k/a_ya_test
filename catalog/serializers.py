from rest_framework import serializers

from catalog.models import Item, Parameter, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['file', 'caption', 'sort_order']


class ParameterSerializer(serializers.ModelSerializer):
    # values = serializers.SerializerMethodField()
    # item_count = serializers.SerializerMethodField('get_item_count')
    #
    # def get_item_count(self, obj):
    #     return obj.item_set.count()

    class Meta:
        model = Parameter
        fields = ['name', 'value', 'price']


class ItemSerializer(serializers.ModelSerializer):
    images = ImageSerializer(source='image_set', many=True, read_only=True)
    parameters = ParameterSerializer(source='parameter_set', many=True, read_only=True)

    class Meta:
        model = Item
        fields = ['images', 'parameters', 'id', 'description', 'base_price', 'sort_order']
