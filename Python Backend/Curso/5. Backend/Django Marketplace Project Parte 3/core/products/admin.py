from django.contrib import admin
from .models import Product, Photo, Tag, Category, Status, Currency

# Register your models here.

class PhotoInLine(admin.StackedInline):
    model = Photo

class TagInLine(admin.TabularInline):
    model = Tag.product_set.through

class CatergoryInLine(admin.TabularInline):
    model = Category.product_set.through

class ProductAdmin(admin.ModelAdmin):
    inlines = [PhotoInLine, TagInLine, CatergoryInLine]

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'singular_name', 'plural_name', 'symbol', 'std_int')

admin.site.register(Photo)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Status)
admin.site.register(Currency, CurrencyAdmin)