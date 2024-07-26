from django.shortcuts import render
from .models import Index


def index(request):
    main = Index.objects.all()
    context = {
        "main": main
    }
    return render(request, 'index.html', context)
