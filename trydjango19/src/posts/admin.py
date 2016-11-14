from django.contrib import admin

# Register your models here.
from .models import Post

#Create ModelAdmin class for model of Admin site
class PostAdmin(admin.ModelAdmin):
    list_display = ["id","title","timestamped","updated"]
    list_display_links = ['title']
    list_filter = ["timestamped","updated"]
    search_fields = ["title","content"]
    save_as = True
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)