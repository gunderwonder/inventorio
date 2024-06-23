import uuid
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Item(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

	name = models.CharField(max_length=200)
	description = models.TextField(blank=True, null=True)
	sku = models.CharField(max_length=200, blank=True, null=True)
	serial_number = models.CharField(max_length=200, blank=True, null=True)

	category = models.ForeignKey('Category', on_delete=models.CASCADE, default=None, blank=True, null=True)
	labels = models.ManyToManyField('Label', default=None, null=True, blank=True)
	vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE, default=None, null=True, blank=True)

	locations = models.ManyToManyField('Location', default=None, blank=True, null=True)

	link = models.URLField(default="", blank=True, null=True)
	thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
	receipt = models.FileField(upload_to='receipts/', blank=True, null=True)
	note = models.TextField(default="", blank=True, null=True)

	quantity = models.IntegerField(default=1)

	purchase_date = models.DateField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Location(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

	name = models.CharField(max_length=200)
	description = models.TextField(default="")

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class ItemAttribute(models.Model):
    item = models.ForeignKey(Item, related_name='attributes', on_delete=models.CASCADE)
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=255)

    class Meta:
        unique_together = ('item', 'key')

class ItemFile(models.Model):
    item = models.ForeignKey(Item, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='item_files/')


class ItemImage(models.Model):
    item = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item_images/')


class Category(MPTTModel):
	name = models.CharField(max_length=100)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class MPTTMeta:
		order_insertion_by = ['name']

	class Meta:
		verbose_name_plural = "categories"

	def __str__(self):
		return self.name


class Label(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

	name = models.CharField(max_length=200)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Vendor(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

	name = models.CharField(max_length=200)
	description = models.TextField(default="")

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name
