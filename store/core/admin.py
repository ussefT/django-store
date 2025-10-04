from django.contrib import admin

# Register your models here.

from . import models

# class how show to admin  
class ProductAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

class LikeAdmin(admin.ModelAdmin):
    pass

# add model to admin 
admin.site.register(models.Product,ProductAdmin)
admin.site.register(models.Tag,TagAdmin)
admin.site.register(models.Comment,CommentAdmin)
admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.Like,LikeAdmin)
