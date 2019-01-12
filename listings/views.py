from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
from .models import Listing


def index(request):
    listings = Listing.objects.all()

    paginator = Paginator(listings, 1)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
