from django.contrib import admin

from actors.models import Actor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_actor', 'birthday', 'nationality')
    search_fields = ('name_actor',)
