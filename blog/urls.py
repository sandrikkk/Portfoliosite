from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostsView.as_view(), name = "blog-list"),
    path("<slug:slug>/", views.post_detail, name = "post-detail-page")
]
