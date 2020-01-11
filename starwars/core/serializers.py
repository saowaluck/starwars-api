from rest_framework import serializers

class PeopleSerializer(serializers.Serializer):
    name = serializers.CharField()
    gender = serializers.CharField()
    homeworld = serializers.CharField()
