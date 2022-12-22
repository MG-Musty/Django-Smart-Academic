from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import get_user_model
User = get_user_model()

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

#from . import views
# for the MVT 
from .models import Teacher
from .forms import TeacherForm

# Create your views here.



def index(request):
    return render(request, "users/index.html")


def apply(request):
    return render(request, "users/apply.html")







def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "users/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "users/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "users/register.html")


# For the form of register Teachers
def teacher_list(request):
    teacher = Teacher.objects.all()
    return render(request,
                  'users/teacher_list.html',
                  {'teacher': teacher})

# for the details diplay of Teachers
def teacher_detail(request, id):
    teacher = Teacher.objects.get(id=id)
    return render(request,
                  'users/teacher_detail.html',
                  {'teacher': teacher})


# for the details of the TeacherForm
def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            # create a new `Teacher` and save it to the db
            teacher = form.save()
            # redirect to the detail page of the teacher we just created
            return HttpResponseRedirect(reverse('teacher-detail', kwargs={'id': teacher.id}))
    else:
        form = TeacherForm()

    return render(request,
                  'users/teacher_create.html',
                  {'form': form})

# The editting / update of the existing teacher profile
def teacher_update(request, id):
    teacher = Teacher.objects.get(id=id)

    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            # update the existing `Teacher` in the database
            form.save()
            # redirect to the detail page of the `Teacher` we just updated
            return HttpResponseRedirect(reverse('teacher-detail', kwargs={'id': teacher.id}))
    else:
        form = TeacherForm(instance=teacher)

    return render(request,
                  'users/teacher_update.html',
                  {'form': form})


# Delete entries for teacher list
def teacher_delete(request, id):
    teacher = Teacher.objects.get(id=id)  # we need this for both GET and POST

    if request.method == 'POST':
        # delete the teacher from the database
        teacher.delete()
        # redirect to the teachers list
        return HttpResponseRedirect(reverse('teacher-list'))

    # no need for an `else` here. If it's a GET request, just continue

    return render(request,
                  'users/teacher_delete.html',
                  {'teacher': teacher})

