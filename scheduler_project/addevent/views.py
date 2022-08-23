from django.shortcuts import render, redirect

from .forms import EventForm


def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EventForm()
        context = {
            'form': form
        }
        return render(request, 'addevent/addevent.html', context)