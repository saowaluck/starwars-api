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
        gender = request.query_params.get('gender', None)

        if gender is not None:
            peoples = People.objects.filter(gender=gender)
        else:
            peoples = People.objects.all()

        peoples_list = []
        for people in peoples:
            serializer = PeopleSerializer(people)

            person = serializer.data
            peoples_list.append(person)

        return Response(peoples_list)

    def post(self, request):
        data = request.data

        serializer = PeopleSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

