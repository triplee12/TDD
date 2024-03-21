from django.shortcuts import redirect, render
from .models import Item


def home_page(request):
    """Home page for To-Do lists."""
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, 'home.html', context)
