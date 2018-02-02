from django.contrib import admin
from app01 import models

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','pub_date',)
    list_editable = ('name','price',)
    filter_horizontal = ('authors',)
    list_per_page = 3
    search_fields = ('id','name','publish__name',)
    list_filter = ('pub_date','publish',)


admin.site.register(models.Author)
admin.site.register(models.Book,BookAdmin)
admin.site.register(models.Publish)
