from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import format_duration
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):

    passcard = get_object_or_404(Passcard, passcode=passcode)

    this_passcard_visits = []
    visits = Visit.objects.filter(passcard=passcard)

    for visit in visits:
        visit_data = {
            'entered_at': visit.entered_at,
            'duration': format_duration(visit.get_duration()),
            'is_strange': visit.is_visit_long()
            }
        this_passcard_visits.append(visit_data)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
        }

    return render(request, 'passcard_info.html', context)
