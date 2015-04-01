from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    (r'^bm/', include('ecl_tools.bulkmail.urls')),

    url(r'^admin/newsletters/newsletter/(\d+)/preview/$', 'ecl_tools.bulkmail.views.preview', name='bulkmail_preview'),

)
