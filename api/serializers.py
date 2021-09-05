from rest_framework import serializers

class TaskSerializer(serializers.Serializer):
   id = serializers.IntegerField()
   title = serializers.CharField()
   description = serializers.CharField()
   status = serializers.BooleanField()