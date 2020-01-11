from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from rest_framework.views import APIView, Response

from core.models import People


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
        peoples = People.objects.all()

        peoples_list = []
        for people in peoples:
            person = {
                'name': people.name,
                'gender': people.gender,
                'homeworld': people.homeworld.name
            }

            peoples_list.append(person)

        return Response(peoples_list)
