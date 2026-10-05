from django.shortcuts import render, redirect, get_object_or_404

from .forms import ContactForm, PortfolioContactForm, TopicForm
from .models import Topic


def base(request):
    return render(request, "base.html")


# ==========================================
# Topics CRUD Views
# ==========================================

def topics(request):
    topics = Topic.objects.all().order_by("name")
    return render(request, "topics.html", {"topics": topics})
    


def topic_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        category = request.POST.get("category")
        description = request.POST.get("description")
        topic = Topic(name=name, category=category, description=description)
        topic.save()
        return redirect("topics")
    else:
        form = TopicForm()
    return render(request, "topic_form.html", {"form": form})


def topic_edit(request, id):
    topic = get_object_or_404(Topic, id=id)

    if request.method == "POST":
        topic.name = request.POST.get("name")
        topic.category = request.POST.get("category")
        topic.description = request.POST.get("description")
        topic.save()
        return redirect("topics")
    
    return render(request, "topic_form.html", {"topic": topic})
 

def topic_delete(request, id):
    topic = get_object_or_404(Topic, id=id)

    if request.method == "POST":
        topic.delete()
        return redirect("topics")

    return render(request, "topic_confirm_delete.html", {"topic": topic})


# ==========================================
# Other LearnHub Views
# ==========================================

def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("contact_success")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})


def contact_success(request):
    return render(request, "contact_success.html")


# ==========================================
# Portfolio Views
# ==========================================

def portfolio_home(request):
    return render(request, "portfolio/home.html")


def portfolio_work(request):
    return render(request, "portfolio/work.html")


def portfolio_expertise(request):
    return render(request, "portfolio/expertise.html")


def portfolio_testimonials(request):
    return render(request, "portfolio/testimonials.html")


def portfolio_aboutme(request):
    return render(request, "portfolio/aboutme.html")


def portfolio_contact(request):
    if request.method == "POST":
        form = PortfolioContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("portfolio_contact_success")
    else:
        form = PortfolioContactForm()

    return render(request, "portfolio/contact.html", {"form": form})


def portfolio_contact_success(request):
    return render(request, "portfolio/contact_success.html")