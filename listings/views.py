from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .choices import state_choices, bedroom_choices, price_choices
# Create your views here.
from .models import Listing


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords
    keywords = request.GET.get('keywords', None)
    if keywords:
        queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    city = request.GET.get('city', None)
    if city:
        queryset_list = queryset_list.filter(city__iexact=city)

    # State
    state = request.GET.get('state', None)
    if state:
        queryset_list = queryset_list.filter(state__iexact=state)

    # Bedrooms
    bedrooms = request.GET.get('bedrooms', None)
    if bedrooms:
        queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Price
    price = request.GET.get('price', None)
    if price:
        queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list
    }
    return render(request, 'listings/search.html', context)
