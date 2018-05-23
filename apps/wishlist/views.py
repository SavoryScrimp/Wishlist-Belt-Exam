from django.shortcuts import render, redirect
from .models import User, Item
# Create your views here.
def index(request):

    return render(request, 'wishlist/index.html')

def register(request):
    user = User.objects.register(request.POST)
    request.session['username'] = request.POST['username']
    return redirect('/dashboard')

def login(request):
    user = User.objects.login(request.POST)
    print(User.objects.all())
    request.session['username'] = request.POST['username']
    return redirect('/dashboard')

def dashboard(request):
    me = User.objects.get(username=request.session['username']).id
    name = User.objects.get(username=request.session['username']).name
    context = {
        'user' : request.session['username'],
        'my_items' : Item.objects.filter(creator=me),
        'listed_items' : Item.objects.filter(users=me),
        'others_items' : Item.objects.exclude(creator=me)
    }
    return render(request, 'wishlist/dashboard.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def addItem(request):

    return render(request, 'wishlist/wish_items/create.html')

def createItem(request):
    item = Item.objects.createItem(request.POST, request.session['username'])
    print(Item.objects.all())
    return redirect('/dashboard')

def deleteItem(request, number):
    item = Item.objects.deleteItem(item_id=number)
    return redirect('/dashboard')

def addList(request, number):
    me = User.objects.get(username=request.session['username']).id
    item = Item.objects.get(id=number)
    item.users.add(me)
    return redirect('/dashboard')

def removeList(request, number):
    me = User.objects.get(username=request.session['username']).id
    item = Item.objects.get(id=number)
    item.users.remove(me)
    return redirect('/dashboard')

def itemView(request, number):
    item = Item.objects.get(id=number)
    context = {
        'item' : item,
    }
    return render(request, 'wishlist/wish_items/item.html', context)


#login 3 characters
#password 8 characers