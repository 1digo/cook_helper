from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import DishesCreateView, DishesDetailsView


urlpatterns = {
    path('dishes/', DishesCreateView.as_view(), name="create"),
    re_path(r'^dishes/(?P<pk>[0-9]+)/$', DishesDetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
