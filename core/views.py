from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Produto

def index(request):
    produtos = Produto.objects.all()

    context = {
        'curso': "Programação Web com Django Framework",
        'outro': "Django é massa",
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    prod = get_object_or_404(Produto, pk=pk)
    context = {
        'produto': prod
    }

    return render(request, 'produto.html', context)


def error404(request, exception):
    return render(request, '404.html')

def error500(request):
    return render(request, '500.html')