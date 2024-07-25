from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import JsonResponse
from django.core import serializers

from django.shortcuts import render
from .models import actionlist

# Create your views here.
@api_view(["POST"])
def newItem(request):
    print("I am here!")
    print(request.method)
    if request.method == "POST":
        print("Request Data:", request.data)
        action = request.data.get("newItem", None)
        newAddition = actionlist(task=action)
        newAddition.save()
        
        return Response({"message":"item added successfully"},status=200)
    


@api_view(["GET"])
def showItem(request):
    print("I am here!")
    if request.method == "GET":
        actions = actionlist.objects.all()
        data = serializers.serialize('json', actions)
        print(data)
        return JsonResponse(data, safe=False, status=200)
    
"""def delItem(request):
    if request.method == "POST":
"""
