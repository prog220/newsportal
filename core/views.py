from django.shortcuts import render, redirect
from .models import New

# Create your views here.
def news_list(request):
    news = New.objects.all()
    return render(request, 'index.html', {'news': news})

def load_page(request):
    id = request.GET.get('id')
    new = New.objects.filter(id=id)
    return render(request, 'article.html', {'news': new})

def create(request):
    return render(request, 'create.html')

def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        anons = request.POST.get('anons')
        text = request.POST.get('text')

        New.objects.create(
            title = title,
            anons =  anons,
            text = text,
        )

        return redirect('/')