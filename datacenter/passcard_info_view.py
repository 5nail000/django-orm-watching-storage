from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import format_duration
from django.shortcuts import render
from django.http import Http404


def passcard_info_view(request, passcode):

    try:
        passcard = Passcard.objects.filter(passcode=passcode)[0]
    except IndexError:
        raise Http404("")

    # Программируем здесь
    this_passcard_visits = []
    visits = Visit.objects.filter(passcard=passcard)

    for visit in visits:
        visit_data = {
            'entered_at': visit.entered_at,
            'duration': format_duration(visit.get_duration()),
            'is_strange': 'ОЧЕНЬ ДОЛГО' if visit.is_visit_long() else ''
            }
        this_passcard_visits.append(visit_data)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
        }

    return render(request, 'passcard_info.html', context)
