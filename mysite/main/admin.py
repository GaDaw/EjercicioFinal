from django.contrib import admin
from .models import *


class FighterAdmin(admin.ModelAdmin):
    list_display = ('alias', 'force', 'skill', 'resistance')
    search_fields = ('alias',)


class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'finish_date', 'fighter_count', 'category')
    list_filter = ('name', 'category', 'fighter_count')
    search_fields = ('name',)
    filter_horizontal = ('dfighters',)


class DisputedtournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'rounds',)    

    

admin.site.register(Fighter, FighterAdmin)
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Disputedtournament, DisputedtournamentAdmin )

# Register your models here.
