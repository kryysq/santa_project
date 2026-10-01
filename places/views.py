import random
from django.shortcuts import render, redirect
from .models import Place, Participant
from .forms import ParticipantForm

def home(request):
    return render(request, 'places/home.html')

def santa_view(request):
    participants = Participant.objects.all()
    
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('santa')
    else:
        form = ParticipantForm()
        
    context = {
        'form': form,
        'participants': participants,
    }
    return render(request, 'places/santa.html', context)

def shuffle_santa(request):
    participants = list(Participant.objects.all())
    if len(participants) > 1:
        #Алгоритм жеребкування
        givers = participants.copy()
        receivers = participants.copy()
        
        #Перемішуємо доти, доки хтось не витягне сам себе
        while any(g == r for g, r in zip(givers, receivers)):
            random.shuffle(receivers)
            
        for g, r in zip(givers, receivers):
            g.assigned_to = r.name
            g.save()
            
    return redirect('santa')
