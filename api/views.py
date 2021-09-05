import json
import re
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status 
from .serializers import TaskSerializer
from pathlib import Path
from rest_framework.response import Response

# Create your views here.

tasks = [
    {
        'id': 1,
        'title': u'Test',
        'description': u'Basis test', 
        'status': False
    },
    {
        'id': 2,
        'title': u'Test1',
        'description':u'Test2', 
        'status': False
    }
]

@api_view(['GET'])
def get_task(request, task_id=None):
    task = None
    for tk in tasks:
        if(tk['id'] == task_id):
            task = tk
    if(task != None): 
        if(request.method == 'GET'):
            return Response(task)
    else:
        return Response({'message': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST', 'GET'])
def create_task(request):
    if(request.method == 'POST'):
        serialiser = TaskSerializer(data=request.data)
        if(serialiser.is_valid()):
            tasks.append(serialiser.data)
            return Response(tasks)
        return Response(serialiser)
    elif(request.method == 'GET'):
        return Response(tasks)


@api_view(['PUT'])
def update_task(request, task_id):
    task = None
    for tk in tasks:
        if(tk['id'] == task_id):
            task = tk
    if(task != None): 
        if(request.method == 'PUT'):
            tasks.remove(task)
            tasks.append(request.data)
            return Response(request.data, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_task(request, task_id):
    task = None
    for tk in tasks:
        if(tk['id'] == task_id):
            task = tk
    if(task != None):  
        if(request.method == 'DELETE'):
            tasks.remove(task)
            return Response({'message': 'Deleted'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
