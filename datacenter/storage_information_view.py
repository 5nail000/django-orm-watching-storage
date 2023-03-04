from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import format_duration
from django.shortcuts import render


def storage_information_view(request):
    # Программируем здесь

    non_closed_visits = []
    visits = Visit.objects.filter(leaved_at=None)
    for visit in visits:
        visit_data = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': format_duration(visit.get_duration()),
            'is_strange': 'ОЧЕНЬ ДОЛГО' if visit.is_visit_long() else ''
            }
        non_closed_visits.append(visit_data)


    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }

    return render(request, 'storage_information.html', context)

    print(request)

    visits = [item for item in Visit.objects.all() if not item.leaved_at]

    #
    not_leaved = []
    for visit in visits:
        print('\n------------------------')
        print(visit.passcard.owner_name)
        not_leaved.append(visit.passcard.owner_name)
        print('Зашёл в хранилище, время по Москве:')
        print(localtime(visit.entered_at))
        delta = datetime.timedelta(seconds=int((localtime() - visit.entered_at).total_seconds()))
        print('\nНаходится в хранилище:')
        print(delta)

    print(not_leaved)
