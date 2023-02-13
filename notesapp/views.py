import django.shortcuts
from django.contrib import messages
from .forms import NotesForm
from .models import Notes
from datetime import datetime

# Create your views here.

def index(request):
    notes = Notes.objects.all()
    return django.shortcuts.render(request, "index.html", {"notes": notes})

def new_note(request):
    form = NotesForm()
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return django.shortcuts.redirect("index")
    else:
        return django.shortcuts.render(request, "update.html", {"form": form})

def note_detail(request, pk):
    note = Notes.objects.get(id=pk)
    form = NotesForm(instance=note)
    if request.method == 'POST':
        note.time= datetime.now()
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return django.shortcuts.redirect("index")
    else:
        return django.shortcuts.render(request, "update.html", {"form": form})

def delete_note(request, pk):
    note = Notes.objects.get(id=pk)
    form = NotesForm(instance=note)
    if request.method == 'POST':
        note.delete()
        messages.info(request, "The note has been deleted")
    return django.shortcuts.render(request, "delete.html", {"form": form})

def search_page(request):
    if request.method == 'POST':
        search_text = request.POST['search']
        notes = Notes.objects.filter(heading__icontains = search_text) | Notes.objects.filter(text__icontains = search_text)
        return django.shortcuts.render(request, "search.html", {"notes": notes})
    else:
        return django.shortcuts.redirect("index")
