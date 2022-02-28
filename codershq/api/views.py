from django.core import serializers
from django.http import JsonResponse

from codershq.events.models import Event


def events(request):
    events = Event.objects.all()
    data = serializers.serialize(
        "json",
        events,
        fields=[
            "title",
            "short_description",
            "date_time",
            "location",
            "image",
            "duration",
            "event_link",
        ],
    )

    return JsonResponse(data, safe=False)
