from django.urls import path
from .views import ContactView, ContactSuccessView

app_name = 'contact'

urlpatterns = [
    path('contacts', ContactView.as_view(), name="contacts"),
    path('success/', ContactSuccessView.as_view(), name="success"),
]