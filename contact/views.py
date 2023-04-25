from django.shortcuts import render, redirect
from .models import Message, ContactWay
from django.contrib.auth.decorators import login_required
from .forms import MessageForm


def message(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = MessageForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                Message.objects.create(user=request.user, content=data.get('content'), email=data.get('email'))
                return redirect('home:home')
        else:
            form = MessageForm
    else:
        form = MessageForm
    contactWay = ContactWay.objects.first()
    return render(request, 'contact/contact.html', context={'form': form, 'contactWay': contactWay})
