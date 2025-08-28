from django.shortcuts import redirect, render

from item.models import Item, Category 
from .forms import SinupForm

def index(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'items': items,
        'categories': categories
    })

def contact(request):
    return render(request, 'core/contact.html')
    
def signup(request):
    if request.method == 'POST':
        form = SinupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SinupForm()
    return render(request, 'core/signup.html', {
        'form': form
    })