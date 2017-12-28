from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from .models import *
from django.views.generic import TemplateView




def index(request):    
    dtournaments_list = Disputedtournament.objects.order_by('name')
    tournament_list = Tournament.objects.order_by('name')[:5]
    fighter_list = Fighter.objects.order_by('alias')[:5]
    template = loader.get_template('main/index.html')
    context = {'tournament_list': tournament_list,
                'fighter_list': fighter_list,
                'dtournaments_list': dtournaments_list,

    }  
    return HttpResponse(template.render(context, request))

def tournaments(request):
    latest_tournament_list = Tournament.objects.order_by('name')    
    template = loader.get_template('main/tournaments.html')
    context = {
        'latest_tournament_list': latest_tournament_list,
    }
    return HttpResponse(template.render(context, request))



def tournament(request, tournament_id):
    tournament = get_object_or_404(Tournament, pk=tournament_id)    
    return render(request, 'main/tournament.html', {'tournament': tournament})

def fighters(request):
    fighter_list = Fighter.objects.order_by('alias')
    template = loader.get_template('main/fighters.html')
    context = {
        'fighter_list': fighter_list,
    }
    return HttpResponse(template.render(context, request))

def fighter(request, fighter_id):
    fighter = get_object_or_404(Fighter, pk=fighter_id)
    return render(request, 'main/fighter.html', {'fighter': fighter})

def tournament_new(request):
    if request.method == "POST":
        form = TournamentForm(request.POST)
        
        if form.is_valid():     
            f =form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('tournaments')
    else:
        form = TournamentForm()
    return render(request, 'main/tournament_edit.html', {'form': form})

def fighter_new(request):
    if request.method == "POST":
        form = FighterForm(request.POST)
        if form.is_valid():              
            form.save()
            return redirect('fighters')
    else:
        form = FighterForm()
    return render(request, 'main/fighter_edit.html', {'form': form})

def initTournament_new(request):
    if request.method == "POST":
        form =  DisputedForm(request.POST)
        if form.is_valid():                        
            f =form.save(commit=False)
            f.save()
            form.save_m2m()  
            

            return redirect('index')
    else:
        form =  DisputedForm()
    return render(request, 'main/disputedtournament_edit.html', {'form': form})

def disputedtournament(request, dtournament_id):
    dtournament = get_object_or_404(Disputedtournament, pk=dtournament_id)
    return render(request, 'main/disputedtournament.html', {'dtournament': dtournament})


def disputedtournaments(request):
    dtournaments_list = Disputedtournament.objects.order_by('name')
    template = loader.get_template('main/disputedtournaments.html')
    context = {
        'dtournaments_list': dtournaments_list,
    }
    return HttpResponse(template.render(context, request))