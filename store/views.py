from django.shortcuts import render
from .models import Vlog

def index(request):
    vlogs = Vlog.objects.all().order_by('-created_at')
    return render(request, 'store/index.html', {'vlogs': vlogs})

def vlog_list(request):
    vlogs = Vlog.objects.all().order_by('-created_at')
    return render(request, 'store/vlog_list.html', {'vlogs': vlogs})