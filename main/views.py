from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as LogIn
from django.contrib.auth import logout as LogOut
from django.shortcuts import render
from django.shortcuts import redirect
from .models import List


def signout(request):
    LogOut(request)
    return redirect(login)


def login(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['email'], password=request.POST['password'])
        LogIn(request, user)
        return redirect(index)
    return render(request, 'main/login.html')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        user2 = User.objects.create_user(username=email, email=email, first_name=name, password=password)
        user2.save()
        return redirect('/')
    return render(request, 'main/register.html')


def deleteItem(request, item_id):
    List.objects.get(id=item_id).delete()
    return redirect('/')


def add(request):
    if request.method == 'POST':
        id = request.user.id
        name = request.POST['title']
        new_item = List(title=name, user_id=id)
        new_item.save()
        return redirect('/')


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'main/welcome.html')
    id = request.user.id
    items = List.objects.filter(user_id=id)
    return render(request, 'main/index.html', {'items': items})
