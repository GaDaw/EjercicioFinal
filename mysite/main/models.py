from django.db import models
from django.forms import ModelForm
from django import forms

class Fighter(models.Model):
    alias = models.CharField('Nombre', max_length=15, primary_key=True)    
    force = models.PositiveIntegerField('Fuerza', default=4)
    skill = models.PositiveIntegerField('Habilidad', default=3)
    resistance = models.PositiveIntegerField('Resistencia', default=3)

    def __str__(self):
        return self.alias

    class Meta:
        verbose_name = 'Luchador'
        verbose_name_plural = 'Luchadores'

TOURNAMENT_CATEGORIES = (
    (0, 'Pluma'),
    (1, 'Tigre'),
    (2, 'León')
)

class Tournament(models.Model):
    name = models.CharField('Nombre', max_length=150, primary_key=True)
    start_date = models.DateTimeField('Hora inicio')
    finish_date = models.DateTimeField('Hora final')
    fighter_count = models.IntegerField('Nº Jugadores')
    category = models.IntegerField('Categoria', choices=TOURNAMENT_CATEGORIES, default=0)
    dfighters = models.ManyToManyField(Fighter, verbose_name='Luchadores')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Torneo'
        verbose_name_plural = 'Torneos'


class Disputedtournament(models.Model):
    #PROTECT No se puede eliminar el torneo al que hace referencia sin eliminar primero el torneo disputado
    name = models.OneToOneField(Tournament,on_delete=models.PROTECT,primary_key=True)
    rounds = models.IntegerField('Nº Rondas por combate')
    
    
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Torneo Disputado'
        verbose_name_plural = 'Torneos Disputados'


        

#---------------FORMULARIOS---------------------------------------------



class DateInput(forms.DateInput):
    input_type = 'date'


class TournamentForm(ModelForm):
    class Meta:
        
        start_date = forms.DateTimeField()
        model = Tournament
        fields = '__all__'
        widgets = {
            'start_date': DateInput(),
            'finish_date': DateInput(),
            'dfighters': forms.CheckboxSelectMultiple()  
        }
           

class FighterForm(ModelForm):
    class Meta:
        model = Fighter
        fields = '__all__'


class DisputedForm(ModelForm):
    class Meta:
        model = Disputedtournament
        fields = ('name', 'rounds')