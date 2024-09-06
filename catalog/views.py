from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from catalog.filters import ItemFilterset
from catalog.models import Item
from catalog.paginators import ItemPaginator
from catalog.serializers import ItemSerializer


# Create your views here.
class ItemListView(ListAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all().prefetch_related('image_set', 'parameter_set')
    filterset_class = ItemFilterset
    pagination_class = ItemPaginator


class ItemDetailView(RetrieveAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all().prefetch_related('image_set', 'parameter_set')
    filterset_class = ItemFilterset
