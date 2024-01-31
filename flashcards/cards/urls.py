from django.urls import path
from . import views

urlpatterns = [
    path("card", views.FlashCardDetail.as_view(), name="view_card"),
    path("create", views.create_card, name="create_card")

]