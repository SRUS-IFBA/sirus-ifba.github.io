from django.contrib import admin
from polls.models import Choice, Poll

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 
		'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)

#admin.site.register(Choice)

# admin.site.register(Poll) padrao

# Mudar o question no historico para baixo
# class PollAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question']
#
# admin.site.register(Poll, PollAdmin)