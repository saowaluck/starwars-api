from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from rest_framework.views import APIView, Response

from core.models import People, Planet
from core.serializers import PeopleSerializer

class PeopleListView(TemplateView):
    def get(self, request):
        people = People.objects.first()

        person = {
            'name': people.name,
            'gender': people.gender,
            'homeworld': people.homeworld.name
        }

        return JsonResponse(person)


class PeopleListAPIView(APIView):
    def get(self, request):
        peoples = People.objects.filter(gender='n/a')

        serializer = PeopleSerializer(peoples, many=True)

        return Response(serializer.data)

    def post(self, request):
        data = request.data

        serializer = PeopleSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

