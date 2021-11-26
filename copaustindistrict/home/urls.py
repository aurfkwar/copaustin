from django.urls import path
from . import views
from .views import ContactView, ContactSuccessView

urlpatterns = [
    path('', views.home),
    path('footer', views.footer, name="footer"),
    path('', views.home, name="index"),
    path('contact', views.contact_us, name="contact"),
    path('donate', views.donate, name="donate"),
    path('tenets', views.tenets, name="tenets"),
    path('childrenministry', views.childrenministry, name="childrenministry"),
    path('evangelismministry', views.evangelism_ministry, name="evangelismministry"),
    path('sermons', views.sermons, name="sermons"),
    path('videos', views.videos, name="videos"),
    path('gallery', views.gallery, name="gallery"),
    path('leadership', views.leadership, name="leadership"),
    path('mensministry', views.mensministry, name="mensministry"),
    path('womensministry', views.womensministry, name="womensministry"),
    path('history', views.history, name="history"),
    path('youthministry', views.youthministry, name="youthministry"),
    path('websitebuilders', views.websitebuilders, name="websitebuilders"),

    path('biblestudies', views.biblestudies, name="biblestudies"),
    path('books', views.books, name="books"),
    path('pentecostsongs', views.pentecostsongs, name="pentecostsongs"),
    path('churchmedia', views.churchmedia, name="churchmedia"),
    path('ministries', views.ministries, name="ministries"),
    path('local', views.local, name="local"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('pastorpage', views.pastorpage, name="pastorpage"),
    path('contact', ContactView.as_view(), name="contact"),
    path('success', ContactSuccessView.as_view(), name="success"),
]