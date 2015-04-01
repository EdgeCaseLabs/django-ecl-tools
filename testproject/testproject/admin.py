from django.contrib import admin
from models import NewsletterSample


class NewsletterSampleAdmin(admin.ModelAdmin):
    list_display = ('title', 'sent', 'scheduled', 'created', 'preview', 'StatsLink')

admin.site.register(NewsletterSample, NewsletterSampleAdmin)

