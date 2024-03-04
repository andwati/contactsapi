from django.urls import path

from .views import ContactDetailView, ContactList

urlpatterns = [
    path("", ContactList.as_view(), name="contacts"),
    path("<int:id>", ContactDetailView.as_view(), name="contact-detail"),
]
