from django.shortcuts import render
from amina.models import Preview

# Create your views here.
def amina(request):
    amina = Preview.objects.all()
    context = {
        'amina': amina
    }
    return render(request, 'amina.html', context)

def bio(request, pk):
    preview = Preview.objects.get(pk=pk)
    context = {
        'preview': preview
    }
    return render(request, 'bio.html', context)

def home(request):
    return render(request, 'home.html')