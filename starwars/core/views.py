from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from rest_framework.views import APIView, Response

from core.models import People, Planet


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
        gender = request.query_params.get('gender', None)

        if gender is not None:
            peoples = People.objects.filter(gender=gender)
        else:
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

    def post(self, request):
        data = request.data

        homeworld = Planet.objects.first()
        person = People.objects.create(
            name=data['name'],
            height=data['height'],
            mass=data['mass'],
            hair_color=data['hair_color'],
            skin_color=data['skin_color'],
            eye_color=data['eye_color'],
            birth_year=data['birth_year'],
            gender=data['gender'],
            homeworld=homeworld
        )

        return_person = {
            'name': person.name,
            'gender': person.gender,
            'homeworld': person.homeworld.name
        }

        return Response(return_person)

