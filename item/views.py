from django.shortcuts import render,get_object_or_404, redirect

from .models import Item, Category, CartItem, Favorite

def items(request):

    query = request.GET.get('query','')
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    category_id = request.GET.get('category', 0)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(name__icontains=query)

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })

def detail(request, pk):

    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items' : related_items
    })

def add_to_favorites(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    Favorite.objects.get_or_create(user=request.user, item=item)
    return redirect('item:items')

def remove_from_favorites(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    Favorite.objects.filter(user=request.user, item=item).delete()
    return redirect('item:items')

def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, item=item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('item:items')

def remove_from_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    CartItem.objects.filter(user=request.user, item=item).delete()
    return redirect('item:items')

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'core/cart.html', {'cart_items': cart_items})

def view_favorites(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'core/favorites.html', {'favorites': favorites})
