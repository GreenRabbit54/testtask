from django.shortcuts import render, redirect
from .models import Account, Task
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, AccountAuthencticationForm, TaskForm
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound


def homepage(request):
    tasks = Task.objects.all()
    return render(request, 'homepage.html', {'tasks': tasks})


def registration_view(request):
    context = {}
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            account = authenticate(email=email, password=password)
            login(request, account)
            return redirect('homepage')
        else:
            context['registration_form '] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/registration.html', context)


def logout_view(request):
    logout(request)
    return redirect('homepage')


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("homepage")

    if request.POST:
        form = AccountAuthencticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect("homepage")
    else:
        form = AccountAuthencticationForm()

    context['login_form'] = form
    return render(request, 'account/login.html', context)


def create(request):
    if request.method == "POST":
        task1 = Task()
        task1.title = request.POST.get("title")
        task1.text = request.POST.get("text")
        task1.timeallow = request.POST.get("timeallow")

        task1.save()
        return HttpResponseRedirect("/")


def edit(request, id):
    tasks = Task.objects.get(id=id)

    form = TaskForm(instance=tasks)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'edit.html', context)



def delete(request, id):
    try:
        tasks = Task.objects.get(id=id)
        tasks.delete()
        return HttpResponseRedirect("/")
    except tasks.DoesNotExist:
        return HttpResponseNotFound("<h2>Task did not fount</h2>")

def eachtask(request,id):
    tasks = Task.objects.get(id=id)
    return render(request, "eachtask.html", {"tasks": tasks})
