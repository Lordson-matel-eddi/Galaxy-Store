from django.shortcuts import render, reverse
from django.views import generic
from .models import Collection
from .forms import CollectionCreateForm



class AllCollectionView(generic.ListView):
    template_name = "collection/all_collection.html"
    queryset = Collection.objects.all
    context_object_name = "collections"


class CollectionCreateView(generic.CreateView):
    template_name = "collection/create_collection.html"
    form_class = CollectionCreateForm
    queryset = Collection.objects.all()

    def get_success_url(self):
        return reverse("collection:all")


class Fendi_All(generic.ListView):
    template_name = "collection/fendi~all.html"
    queryset = Collection.objects.filter(brand="fendi")
    context_object_name = "collection"


class Balenciaga_All(generic.ListView):
    template_name = "collection/balen~all.html"
    queryset = Collection.objects.filter(brand="balenciaga")
    context_object_name = "collection"
