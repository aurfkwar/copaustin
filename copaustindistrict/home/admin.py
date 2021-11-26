from django.contrib import admin
from .models import BibleStudy, Books, ChildrenMinistry, DistrictExecutive, EvangelismMinistry, Gallery, MenMinistry, NationalHead, PastorMessage, PentecostSongs, RegionalHead, Sermons, Video, HomePageSlideshow, AnnouncementPage, WomenMinistry, YouthMinistry

# Register your models here.
admin.site.site_header = 'COPAUSTIN District Admin Dashboard'

admin.site.register(Video)
admin.site.register(PastorMessage)
admin.site.register(AnnouncementPage)
admin.site.register(HomePageSlideshow)
admin.site.register(NationalHead)
admin.site.register(RegionalHead)
admin.site.register(DistrictExecutive)
admin.site.register(ChildrenMinistry)
admin.site.register(EvangelismMinistry)
admin.site.register(MenMinistry)
admin.site.register(WomenMinistry)
admin.site.register(YouthMinistry)
admin.site.register(PentecostSongs)
admin.site.register(Books)
admin.site.register(BibleStudy)
admin.site.register(Gallery)
admin.site.register(Sermons)
