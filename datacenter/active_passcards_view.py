import datetime
from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import format_duration
from django.utils.timezone import localtime
from django.shortcuts import render


def active_passcards_view(request):
    # Программируем здесь

    all_passcards = Passcard.objects.filter(is_active=True)
    context = {
        'active_passcards': all_passcards,  # люди с активными пропусками
    }

    return render(request, 'active_passcards.html', context)
