from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.

class Video(models.Model):
    video_title =models.CharField(max_length=100)
    video=models.FileField(upload_to="video/")
   
    def __str__(self):
        return self.video_title

class PastorMessage(models.Model):
    message_title =models.CharField(max_length=100)
    # video_message =models.FileField(upload_to="video/")
    video_message =models.CharField(max_length=500)
    
    class Meta:
        verbose_name_plural="Pastor Message"


    def __str__(self):
        return self.message_title


class HomePageSlideshow(models.Model):
    slide_title =models.CharField(max_length=250, blank=True)
    slideshow_image1 =models.FileField(blank=True)
    slideshow_image2 =models.FileField(blank=True)
    slideshow_image3 =models.FileField(blank=True)

    class Meta:
        verbose_name_plural="HomePage Slideshow"

    def __str__(self):
        return self.slide_title

class AnnouncementPage(models.Model):
    announcement_title =models.CharField(max_length=100)
    # body =models.TextField(null=True, blank=True)
    announcementImg1 = models.FileField(blank=True)
    # announcementImg2 = models.FileField(blank=True)
    # announcementImg3 = models.FileField(blank=True)
    # announcementImg4 = models.FileField(blank=True, null=True)

    class Meta:
        verbose_name_plural="Announcement Page"

    def __str__(self):
        return self.announcement_title

class NationalHead(models.Model):
    nationalhead_name =models.CharField(max_length=100)
    nationalheadImg = models.FileField()

    

    def __str__(self):
        return self.nationalhead_name

    class Meta:
        verbose_name_plural="National Head"
    

class RegionalHead(models.Model):
    regionalhead_name =models.CharField(max_length=100)
    regionalheadImg = models.FileField()

    def __str__(self):
        return self.regionalhead_name

    class Meta:
        verbose_name_plural="Regional Head"


class DistrictExecutive(models.Model):
    districtpastor_name=models.CharField(max_length=100, verbose_name="District Pastor's Name")
    districtpastorImg=models.FileField(verbose_name="District Pastor's Image")
    districtsec_name=models.CharField(max_length=100, verbose_name="District Secretary's Name")
    districtsecImg=models.FileField(verbose_name="District Secretary's Image")
    districtfin_name=models.CharField(max_length=100, verbose_name="District Financial Secretary's Name")
    districtfinImg=models.FileField(verbose_name="District Financial Secretary's Image")
    districtfincom_name=models.CharField(max_length=100, verbose_name="District Financial Committee Chairman's Name")
    districtfincomImg=models.FileField(verbose_name="District Financial Committee Chairman's Image")
    districtmember1_name=models.CharField(max_length=100, verbose_name="District Exec Member Name")
    districtmember1Img=models.FileField(verbose_name="District Exec Member Image")
    districtmember2_name=models.CharField(max_length=100, verbose_name="District Exec Member Name")
    districtmember2Img=models.FileField(verbose_name="District Exec Member Image")
    districtmember3_name=models.CharField(max_length=100, verbose_name="District Exec Member Name")
    districtmember3Img=models.FileField(verbose_name="District Exec Member Image")

    class Meta:
        verbose_name_plural="District Executives"
        



class ChildrenMinistry(models.Model):
    childrenleader_name =models.CharField(max_length=100, verbose_name="District Leader's Name")
    childrenleaderImg = models.FileField(verbose_name="District Leader's Image")
    childrenslide1=models.FileField(verbose_name="Children Slide")
    childrenslide2=models.FileField(blank=True, verbose_name="Children Slide")
    childrenslide3=models.FileField(blank=True, verbose_name="Children Slide")

    def __str__(self):
        return self.childrenleader_name

    class Meta:
        verbose_name_plural="Children Ministry"


class EvangelismMinistry(models.Model):
    evangelismleader_name =models.CharField(max_length=100, verbose_name="District Leader's Name")
    evangelismleaderImg = models.FileField(verbose_name="District Leader's Image")
    evangelismslide1=models.FileField(verbose_name="Evangelism Slide")
    evangelismslide2=models.FileField(blank=True, verbose_name="Evangelism Slide")
    evangelismslide3=models.FileField(blank=True, verbose_name="Evangelism Slide")

    def __str__(self):
        return self.evangelismleader_name

    class Meta:
        verbose_name_plural="Evangelism Ministry"



class MenMinistry(models.Model):
    menleader_name =models.CharField(max_length=100, verbose_name="District Leader's Name")
    menleaderImg = models.FileField(verbose_name="District Leader's Image")
    menslide1=models.FileField(verbose_name="Men's Slide")
    menslide2=models.FileField(blank=True, verbose_name="Men's Slide")
    menslide3=models.FileField(blank=True, verbose_name="Men's Slide")

    def __str__(self):
        return self.menleader_name

    class Meta:
        verbose_name_plural="Men's Ministry"


class WomenMinistry(models.Model):
    womenleader_name =models.CharField(max_length=100, verbose_name="District Leader's Name")
    womenleaderImg = models.FileField(verbose_name="District Leader's Image")
    womenslide1=models.FileField(verbose_name="Women's Slide")
    womenslide2=models.FileField(blank=True, verbose_name="Women's Slide")
    womenslide3=models.FileField(blank=True, verbose_name="Women's Slide")

    def __str__(self):
        return self.womenleader_name

    class Meta:
        verbose_name_plural="Women's Ministry"


class YouthMinistry(models.Model):
    youthleader_name =models.CharField(max_length=100, verbose_name="District Leader's Name")
    youthleaderImg = models.FileField(verbose_name="District Leader's Image")
    campusslide=models.FileField(verbose_name="Campus Slide")
    youthslide1=models.FileField(blank=True, verbose_name="Youth & Pensa Slide")
    youthslide2=models.FileField(blank=True, verbose_name="Youth & Pensa Slide")
    youthslide3=models.FileField(blank=True, verbose_name="Youth & Pensa Slide")

    class Meta:
        verbose_name_plural="Youth & Pensa"


    def __str__(self):
        return self.youthleader_name


class BibleStudy(models.Model):
    studyname =models.CharField(max_length=100, verbose_name="Bible Study Manual Name")
    studyurl=models.URLField(verbose_name="Bible Study Manual URL from AWS")
    
    class Meta:
        verbose_name_plural="Bible Study Manual"


    def __str__(self):
        return self.studyname
   

class PentecostSongs(models.Model):
    hymnbookname =models.CharField(max_length=100, verbose_name="Hymn Book Name")
    hymnbookurl=models.URLField(verbose_name="Hymn Book URL from ABS")
    
    class Meta:
        verbose_name_plural="Pentecost Songs"


    def __str__(self):
        return self.hymnbookname


class Books(models.Model):
    book_title=models.CharField(max_length=100, verbose_name="Book Title")
    bookurl=models.URLField(verbose_name="Book URL from ABS")
    
    class Meta:
        verbose_name_plural="Inspirational Books"


    def __str__(self):
        return self.book_title
   

class Gallery(models.Model):
    gallery_title =models.CharField(max_length=100, verbose_name="Image Title")
    galleryImg=models.FileField(verbose_name="Image")
    

    def __str__(self):
        return self.gallery_title

    class Meta:
        verbose_name_plural="Galleries"



class Sermons(models.Model):
    message_title =models.CharField(max_length=100, verbose_name="Service Title or Date")
    # video_message =models.FileField(upload_to="video/")
    video_message =models.CharField(max_length=500, verbose_name=   "Paste Facebook or Youtube embed code here")
    
    class Meta:
        verbose_name_plural="Live Service"


    def __str__(self):
        return self.message_title