from django.contrib import admin

from mptt.admin import MPTTModelAdmin
from .models import Item, Location, ItemAttribute, Category, Label, Vendor, ItemFile, ItemImage

from unfold.admin import ModelAdmin
from unfold.decorators import display

from django.templatetags.static import static


class ItemAttributeInline(admin.TabularInline):
    model = ItemAttribute
    extra = 1

class ItemImageInline(admin.TabularInline):
    model = ItemImage

class ItemFileInline(admin.TabularInline):
    model = ItemFile

class CategoryAdmin(ModelAdmin):
	list_display = ['name', 'parent']

@admin.register(Item)
class ItemAdmin(ModelAdmin):

	@display(label=True)
	def show_category_as_label(self, obj):
		return obj.category

	@display(label=True)
	def show_labels_as_label(self, obj):
		return [label.name for label in obj.labels.all()]

	@display(label=True)
	def show_locations_as_label(self, obj):
		return [location.name for location in obj.locations.all()]

	@display(header=True)
	def show_header(self, obj):
		return [
			obj.name,
			obj.description,
			obj.initials(),
			{
				"path": obj.thumbnail_url(),  # Path to image
				"squared": True, # Picture is displayed in square format, if empty circle
				"borderless": False  # Picture will be displayed without border
			}
		]

	show_category_as_label.short_description = "Category"
	show_header.short_description = "Item"
	show_labels_as_label.short_description = "Labels"
	show_locations_as_label.short_description = "Locations"

	inlines = [ItemImageInline, ItemFileInline, ItemAttributeInline]
	list_display = ['show_header', 'show_category_as_label', 'show_labels_as_label', 'show_locations_as_label', 'quantity']

@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
	pass

@admin.register(Vendor)
class VendorAdmin(ModelAdmin):
	pass


@admin.register(Label)
class LabelAdmin(ModelAdmin):
	pass

#admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Location)


