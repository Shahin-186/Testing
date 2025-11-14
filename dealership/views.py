from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Car

# Create your views here.

def home(request):
    """Home page view showing featured cars."""
    featured_cars = Car.objects.filter(is_available=True)[:6]
    context = {
        'featured_cars': featured_cars,
        'total_cars': Car.objects.filter(is_available=True).count()
    }
    return render(request, 'dealership/home.html', context)


class CarListView(ListView):
    """View for listing all available cars."""
    model = Car
    template_name = 'dealership/car_list.html'
    context_object_name = 'cars'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = Car.objects.filter(is_available=True)
        
        # Filter by condition
        condition = self.request.GET.get('condition')
        if condition:
            queryset = queryset.filter(condition=condition)
        
        # Filter by make
        make = self.request.GET.get('make')
        if make:
            queryset = queryset.filter(make__iexact=make)
        
        # Filter by max price
        max_price = self.request.GET.get('max_price')
        if max_price:
            try:
                queryset = queryset.filter(price__lte=float(max_price))
            except ValueError:
                pass
        
        return queryset


class CarDetailView(DetailView):
    """View for displaying detailed information about a single car."""
    model = Car
    template_name = 'dealership/car_detail.html'
    context_object_name = 'car'

