from django.urls import path
from model.views.view_list import CardsListView
from model.views.detail_view import CardDetailView

urlpatterns = [
    path("cards/", CardsListView.as_view(), name="cards-list"),
    path("cards/<uuid:card_id>/", CardDetailView.as_view(), name="card-detail"),
]
