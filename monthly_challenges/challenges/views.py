from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string

# Create your views here.
monthly_challenges = {
    "january": "Dry January: Avoid alcohol for the entire month to reset your health.",
    "february": "Fitness February: Complete 30 minutes of daily physical activity.",
    "march": "Mindfulness March: Meditate for 10 minutes every morning.",
    "april": "Active April: Take 10,000 steps every single day.",
    "may": "Minimalist May: Declutter one item from your home each day.",
    "june": "Journaling June: Write down three things you are grateful for every evening.",
    "july": "No-Spend July: Buy only essential groceries and needs; stop impulse shopping.",
    "august": "August Hydration: Drink at least 3 litres of water daily.",
    "september": "Screen-Free September: No social media usage after 8:00 PM.",
    "october": "Open-Minded October: Read one non-fiction book every week.",
    "november": "Nutrition November: Cook all your meals at home and avoid fast food.",
    "december": None
}


def index(request):
    months = list(monthly_challenges.keys())
    response_data = ''
    return render(request, 'challenges/index.html', {
        "months": monthly_challenges.keys()
    })


def monthly_challenges_by_number(request, m):
    months = list(monthly_challenges.keys())
    try:
        redirect_to_month = months[m-1]
        redirect_path = reverse("month-challenge", args=[redirect_to_month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound(f"<h3>{'Invalid month : enter months between 1 to 12'}</h3>")


def monthly_challenge(request, m):
    if m in monthly_challenges:
        home_path = reverse('back-to-all-challenges')
        challenge_text = monthly_challenges[m]
        # return HttpResponse(f'<h1>{monthly_challenges[m]}</h1> <a href={home_path} > home </a>')
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        return render(request, 'challenges/challenge.html', {
            'text': challenge_text,
            'month': m
        })
    else:
        return HttpResponseNotFound(f"<h2>{'this month not supported'}</h2>")
