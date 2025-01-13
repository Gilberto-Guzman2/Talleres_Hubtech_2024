from django.contrib import admin
from .models import Product, Photo, Tag, Category

# Register your models here.

class PhotoInLine(admin.StackedInline):
    model = Photo

class TagInLine(admin.TabularInline):
    model = Tag.product_set.through

class CatergoryInLine(admin.TabularInline):
    model = Category.product_set.through

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [PhotoInLine, TagInLine, CatergoryInLine]

admin.site.register(Photo)
admin.site.register(Tag)
admin.site.register(Category)