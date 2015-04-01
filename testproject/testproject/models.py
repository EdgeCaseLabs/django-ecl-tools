from django.db import models
from ecl_tools.bulkmail.models import TrackingEvent, BaseBulkmailModel

class NewsletterSample(BaseBulkmailModel):
    title = models.CharField(max_length=60)

    def StatsLink(self):
        return '<a href="/bm/stats/'+str(self.id)+'">Stats</a>'
    StatsLink.allow_tags = True

    def get_subject(self):
        return self.title

    def utm_source(self):
        return 'newsletter'

    def get_campaign_id(self):
        return 'newsletter_%d' % (
            self.id)




class CampaignResolver(object):
    def get_model(self):
        return NewsletterSample

    def get(self, *args, **kwargs):
        return NewsletterSample.objects.get(id=kwargs['pk'])
