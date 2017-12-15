from django.contrib import admin
from .models import Post
from .models import Comment


# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('text', 'post')
#     list_filter = (
#         ('post', admin.RelatedOnlyFieldListFilter),
#     )

admin.site.register(Post)
# admin.site.register(Comment, CommentAdmin)
admin.site.register(Comment)