from django.urls import path
from . import views
from .views import profile_view

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("aboutus/", views.AboutUsPageView.as_view(), name="aboutus"),
    path("blog/", views.BlogListView.as_view(), name="blog_list"),
    path("blog/<int:pk>/", views.BlogDetailView.as_view(), name="blog_detail"),
    path("profile/", profile_view, name="profile"),
]
