from django.urls import path

from catalog.views import ItemListView, ItemDetailView
urlpatterns = [
    path('items/', ItemListView.as_view()),
    path('items/<pk>/', ItemDetailView.as_view()),
]
