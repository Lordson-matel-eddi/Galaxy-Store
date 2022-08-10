from django.urls import path
from .views import AllCollectionView, CollectionCreateView, Fendi_All, Balenciaga_All


app_name="collection"

urlpatterns = [
    path("all/", AllCollectionView.as_view(), name="all" ),
    path("fendi/", Fendi_All.as_view(), name="fendi"),
    path("balenciaga/", Balenciaga_All.as_view(), name="balenciaga"),
    path("create/", CollectionCreateView.as_view(), name="create"),
]