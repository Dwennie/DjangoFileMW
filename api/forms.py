from django import forms
from .models import Contact, PortfolioContact, Topic


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "subject", "message"]


class PortfolioContactForm(forms.ModelForm):
    class Meta:
        model = PortfolioContact
        fields = ["name", "email", "subject", "message", "portfolio_url"]

    def clean_portfolio_url(self):
        url = self.cleaned_data.get("portfolio_url")
        if url and not url.startswith(("http://", "https://")):
            url = f"https://{url}"
        return url


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["name", "category", "description"]