import random
from django.shortcuts import render, redirect
from .models import Participant
from .forms import ParticipantForm
from datetime import datetime

def home(request):
    now = datetime.now()
    if now.month == 12 and now.day == 25:
        is_christmas = "Yes"
    else:
        is_christmas = "No"

    return render(request, 'places/home.html', {'is_christmas': is_christmas})

def santa_view(request):
    participants = Participant.objects.all()
    
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('santa')
    else:
        form = ParticipantForm()

    error = request.session.pop('santa_error', None)
        
    context = {
        'form': form,
        'participants': participants,
        'error': error,
    }
    return render(request, 'places/santa.html', context)

def shuffle_santa(request):
   if request.method == 'POST':
        participants = list(Participant.objects.all())
        
        # ВАЛІДАЦІЯ: перевіряємо, чи достатньо учасників
        if len(participants) < 2:
            request.session['santa_error'] = 'Для проведення жеребкування потрібно щонайменше 2 учасники!'
            return redirect('santa')
        
        givers = participants.copy()
        receivers = participants.copy()
        
        # Алгоритм, щоб ніхто не дарував сам собі
        while any(g == r for g, r in zip(givers, receivers)):
            random.shuffle(receivers)

        for giver, receiver in zip(givers, receivers):
            giver.assigned_to = receiver.name
            giver.save()

        return redirect('santa')
