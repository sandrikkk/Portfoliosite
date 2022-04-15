from django.contrib import admin
from .models import Category, Portfolio
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ('category_name', 'slug')
admin.site.register(Category, CategoryAdmin)

class slug(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title', 'slug') 
admin.site.register(Portfolio,slug)