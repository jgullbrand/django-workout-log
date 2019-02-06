from django.shortcuts import render, redirect
from .models import GymEntry
from .forms import EntryForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	entries = GymEntry.objects.filter(owner=request.user).order_by("-id")
	context = {"entries" : entries}
	return render(request, "workout_entries/index.html", context)

@login_required
def add(request):
	form = EntryForm(request.POST)
	if form.is_valid():
		new_entry = form.save(commit=False)
		new_entry.owner = request.user
		new_entry.save()
		return redirect('index')
	context = {"form": form}
	return render(request, "workout_entries/add.html", context)	

def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password1"]
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect("index")
	else:
		form = UserCreationForm()

	context = {"form": form}
	return render(request, "registration/register.html", context)

def logout(request):
	logout(request)
	return redirect("login")
