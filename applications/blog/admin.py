from django.contrib import admin

from applications.blog.models import Blog, Campaign, Replies, Tags

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'blog_id', 'title', 'author', 'date_added', 'updated_at', 'blog_type', 'campaign_id',
    )
    ordering = [('-date_added'), ]
    search_fields = ['blog_id', 'title', 'author', 'blog_type', 'campaign_id']
    
class CampaignAdmin(admin.ModelAdmin):
    list_display = (
        'campaign_id', 'name', 'date_started', 'date_ended',
    )
    ordering = [('-date_started'), ]
    search_fields = ['campaign_id', 'name',]

class RepliesAdmin(admin.ModelAdmin):
    list_display = (
        'reply_id', 'blog_id', 'author', 'parent_reply_id', 'time_stamp',
    )
    ordering = [('-time_stamp')]
    search_fields = ['sender', 'blog_id']


class TagsAdmin(admin.ModelAdmin):
    list_display = ('tag_name', 'date_added', 'last_modified')
    ordering = ['tag_name']
    search_fields = ['tag_name']

admin.site.register(Blog, BlogAdmin)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Replies, RepliesAdmin)
admin.site.register(Tags, TagsAdmin)