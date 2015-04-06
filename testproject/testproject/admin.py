from django.contrib import admin
from ecl_tools.utils.admin import CommonAdmin
from models import NewsletterSample


class NewsletterSampleAdmin(CommonAdmin):
    list_display = ('title', 'sent', 'scheduled', 'created', 'preview', 'StatsLink')

admin.site.register(NewsletterSample, NewsletterSampleAdmin)

