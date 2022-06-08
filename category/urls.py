from django.urls import path
from . import views

urlpatterns = [
    path("", views.portfolio, name = "all-works"),
    path("<slug:category_slug>/", views.portfolio, name = "programs_by_category"),
    path("<slug:category_slug>/<slug:program_slug>/", views.portfolio_detail, name = "programs_detail")
]
