from django.contrib import admin

from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Item, Location, ItemAttribute, Category, Label, Vendor, ItemFile, ItemImage


class ItemAttributeInline(admin.TabularInline):
    model = ItemAttribute
    extra = 1


class ItemImageInline(admin.TabularInline):
    model = ItemImage

class ItemFileInline(admin.TabularInline):
    model = ItemFile


class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImageInline, ItemFileInline, ItemAttributeInline]


admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Location)
admin.site.register(Label)
admin.site.register(Vendor)


