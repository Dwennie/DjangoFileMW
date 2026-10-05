from django.urls import path
from . import views

urlpatterns = [
    # LearnHub Routes
    path("", views.base, name="home"),
    path("learnhub/", views.base, name="learnhub_home"),

    # Topics CRUD Routes
    path("topics/", views.topics, name="topics"),
    path("topics/new/", views.topic_create, name="topic_create"),
    path("topics/<int:id>/edit/", views.topic_edit, name="topic_edit"),
    path("topics/<int:id>/delete/", views.topic_delete, name="topic_delete"),

    # Other LearnHub Routes
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("contact/success/", views.contact_success, name="contact_success"),

    # Portfolio Routes
    path("portfolio/", views.portfolio_home, name="portfolio_home"),
    path("portfolio/work/", views.portfolio_work, name="portfolio_work"),
    path("portfolio/expertise/", views.portfolio_expertise, name="portfolio_expertise"),
    path("portfolio/testimonials/", views.portfolio_testimonials, name="portfolio_testimonials"),
    path("portfolio/about/", views.portfolio_aboutme, name="portfolio_aboutme"),
    path("portfolio/contact/", views.portfolio_contact, name="portfolio_contact"),
    path("portfolio/contact/success/", views.portfolio_contact_success, name="portfolio_contact_success"),
]