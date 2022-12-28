from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
challenges = {
    "january": "Don't eat meat for a month!",
    "february": "Walk at least 5000 steps!",
    "march": "Learn Django for 30 minutes every day!",
    "april": "Don't eat meat for a month!",
    "may": "Walk at least 5000 steps!",
    "june": "Learn Django for 30 minutes every day!",
    "july": "Don't eat meat for a month!",
    "august": "Walk at least 5000 steps!",
    "september": "Learn Django for 30 minutes every day!",
    "october": "Don't eat meat for a month!",
    "november": "Walk at least 5000 steps!",
    "december": "Learn Django for 30 minutes every day!",
}

def index(request):
    list_items = ""
    months = list(challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        reverse_path = reverse("month-challenge", args=[month])
        list_items += f'<li><a href="{reverse_path}">{capitalized_month}</li>'

    html_data = f"<ul>{list_items}</ul>"
    return HttpResponse(html_data)

def monthly_challenge_by_number(request, month):
    try:
        months = list(challenges.keys())
        redirected_month = months[month - 1]

        redirect_url = reverse("month-challenge", args=[redirected_month])
        return HttpResponseRedirect(redirect_url)
    except:
        return HttpResponseNotFound("This month is unavailable.")
    

def monthly_challenge(request, month):
    try:
        challenge_text = challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is unavailable.</h1>")
    
