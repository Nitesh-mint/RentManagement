from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from .models import Room

@login_required(login_url='login')
def index(request):
    context = {
        'user': request.user
    }
    return render(request, 'index.html', context)

def rooms(request):
    room = Room.objects.all()
    return render(request, "room.html", context={"room":room})

def payment_done(request):
    return render(request, 'payment.html')