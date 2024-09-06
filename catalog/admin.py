from django.contrib import admin

from catalog.models import Image, Parameter, Item


class ImageAdmin(admin.TabularInline):
    model = Image
    extra = 1


class ParameterAdmin(admin.TabularInline):
    model = Parameter
    extra = 1


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'base_price', 'sort_order')
    inlines = [ImageAdmin, ParameterAdmin]


admin.site.register(Image)
admin.site.register(Parameter)
