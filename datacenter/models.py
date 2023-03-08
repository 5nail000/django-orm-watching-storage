import math
from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        leaved_at = localtime() if not self.leaved_at else self.leaved_at
        duration = int((leaved_at - self.entered_at).total_seconds())
        return duration

    def is_visit_long(self):
        return self.get_duration() > 3600


def format_duration(seconds):

    if not seconds:
        return " --- "

    if seconds < 1:
        return '0 секунд'

    text_time = ''

    if seconds > 3600:
        hours = math.floor(seconds/3600)
        solver = int(str(hours)[-1]) if hours >= 21 else hours
        temp_str = 'час' if solver < 2 else ('часа' if solver < 5 else 'часов')
        if solver < 1:
            temp_str = 'часов'
        text_time += f"{hours} {temp_str} "
        seconds = seconds - hours*3600
    if seconds > 60:
        minutes = math.floor(seconds/60)
        solver = int(str(minutes)[-1]) if minutes >= 21 else minutes
        temp_str = 'минута' if solver < 2 else ('минуты' if solver < 5 else 'минут')
        if solver < 1:
            temp_str = 'минут'
        text_time += f"{minutes} {temp_str} "
        seconds = seconds - minutes*60
    if seconds > 0:
        solver = int(str(seconds)[-1]) if seconds >= 21 else seconds
        temp_str = 'секунда' if solver < 2 else ('секунды' if solver < 5 else 'секунд')
        text_time += f"{seconds} {temp_str} "

    text_time = text_time[:-1]

    return text_time
