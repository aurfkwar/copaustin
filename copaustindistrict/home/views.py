from django.shortcuts import render
from django.http import HttpResponse
from .models import BibleStudy, Books, ChildrenMinistry, DistrictExecutive, EvangelismMinistry, Gallery, MenMinistry, NationalHead, PastorMessage, PentecostSongs, RegionalHead, Sermons, Video, HomePageSlideshow, AnnouncementPage, WomenMinistry, YouthMinistry
from django.views.generic import FormView, TemplateView
from .forms import ContactForm
from django.urls import reverse_lazy

# Create your views here.
# def home(request):
#     return render(request, "index.html")

def footer(request):
    return render(request, "footer.html")

def home(request):
    homepageslide=HomePageSlideshow.objects.all()
    homepageannouncement=AnnouncementPage.objects.all()
    return render(request, "index.html", {
        "homepageslide":homepageslide,
        "homepageannouncement":homepageannouncement
        })

def contact_us(request):
    return render(request, "contact.html")

def donate(request):
    return render(request, "donate.html")

def tenets(request):
    return render(request, "tenets.html")

def childrenministry(request):
    childministry=ChildrenMinistry.objects.all()
    return render(request, "childrenministry.html", {"childministry":childministry})


def evangelism_ministry(request):
    evangministry=EvangelismMinistry.objects.all()
    return render(request, "evangelismministry.html", {"evangministry":evangministry})

def sermons(request):
    sermon=Sermons.objects.all()
    return render(request, "sermons.html", {"sermon":sermon})

def videos(request):
    video=Video.objects.all()
    # video1=Item.objects.all()
    return render(request, "videos.html", {"video":video})

def gallery(request):
    photos=Gallery.objects.all()
    return render(request, "gallery.html", {"photos":photos})

def leadership(request):
    nationalhead=NationalHead.objects.all()
    regionalhead=RegionalHead.objects.all()
    districtexecutives=DistrictExecutive.objects.all()
    return render(request, "leadership.html", {
        "nationalhead":nationalhead,
        "regionalhead":regionalhead,
        "districtexecutives":districtexecutives,
        })

def mensministry(request):
    menministry=MenMinistry.objects.all()
    return render(request, "mensministry.html", {"menministry":menministry})

def womensministry(request):
    womenministry=WomenMinistry.objects.all()
    return render(request, "womensministry.html", {"womenministry":womenministry})

def history(request):
    return render(request, "history.html")

def youthministry(request):
    youth=YouthMinistry.objects.all()
    return render(request, "youthministry.html", {"youth":youth})

def websitebuilders(request):
    return render(request, "websitebuilders.html")

def biblestudies(request):
    biblestudy=BibleStudy.objects.all()
    return render(request, "biblestudies.html", {"biblestudy":biblestudy})

def books(request):
    book=Books.objects.all()
    return render(request, "books.html", {"book":book})

def pentecostsongs(request):
    hymnbook=PentecostSongs.objects.all()
    return render(request, "pentecostsongs.html", {"hymnbook":hymnbook})

def churchmedia(request):
    return render(request, "churchmedia.html")

def ministries(request):
    return render(request, "ministries.html")

def local(request):
    return render(request, "local.html")

def aboutus(request):
    return render(request, "aboutus.html")

def pastorpage(request):
    video_message=PastorMessage.objects.all()
    
    return render(request, "pastorpage.html", {"video_message":video_message})

# def slides(request):
#     homepageslide=HomePageSlideshow.objects.all()
#     return render(request, "index.html", {"homepageslide":homepageslide})


# def announcement_home(request):
#     homepageannouncement=AnnouncementPage.objects.all()
#     return render(request, "index.html", {"homepageannouncement":homepageannouncement})

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)

class ContactSuccessView(TemplateView):
    template_name = 'success.html'


   

