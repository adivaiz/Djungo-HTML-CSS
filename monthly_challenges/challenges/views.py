from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse


monthly_challenges={
    "january":"Eat no meat for the entire month",
    "February": "walk for at least 20 minutes every day!",
    "march":"learn Django for at least 20 minutes every day",
    "april":"Eat no meat for the entire month",
    "may": "walk for at least 20 minutes every day!",
    "june":"learn Django for at least 20 minutes every day",
    "july":"Eat no meat for the entire month",
    "august":"walk for at least 20 minutes every day!",
    "september":"learn Django for at least 20 minutes every day",
    "october":"Eat no meat for the entire month",
    "november":"walk for at least 20 minutes every day!",
    "december": None
}
def index(request):
    months=list(monthly_challenges.keys())
    return render(request,"challenges/index.html",{
        "months":months
    })

def monthly_challenge(request,month):
    try:
        challenge_text=monthly_challenges[month] 
        return render(request,"challenges/challenges.html",{
            "text":challenge_text,
            "month_name":month} )  
    except:
        return HttpResponseNotFound("<h1>this month not supported</h1>") 
    
def monthly_challenge_by_number(request,month):
    months=list(monthly_challenges.keys())
    if month>len(months):
        return HttpResponseNotFound("invalid month")
    redirect_month=months[month-1]
    redirect_path=reverse("month_challenge",args=[redirect_month])
    return HttpResponseRedirect(redirect_path)            
        


