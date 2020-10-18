from django.shortcuts import render, HttpResponse
from home.models import Note


# Create your views here.
def home(request):
    context = {'success': False}
    if request.method == "POST":
              #Handle the form
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        ins = Note( note_title = title, note_desc=desc)
        ins.save()
        context = {'success': True}
    return render(request, 'index.html', context)
def Notes(request):
    return render(request, 'note.html')



