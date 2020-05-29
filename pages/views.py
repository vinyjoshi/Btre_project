from django.shortcuts import render
from .choices import state_choices, price_choices, bedroom_choices
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    
    context = {
        'listings': listings,
        'state_choices' : state_choices,
        'bedroom_choices' : bedroom_choices,
        'price_choices' : price_choices,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    realtors = Realtor.objects.all()
    mvp_realtor = Realtor.objects.filter(is_mvp=True)
    
    context = {
        'realtors' : realtors,
        'mvp_realtor' : mvp_realtor,    
    }
    return render(request, 'pages/about.html', context)
