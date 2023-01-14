from django.shortcuts import render, redirect
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Advocate, Company
from .serializers import AdvocateSerializer, CompanySerializer
# Create your views here.


# GET /advocates - get list of advocates
# POST /advocates -

# GET /advocates/:id  - get a single advocate
# PUT /advocates/:id - update a single advocate
# DELETE /advocates/:id - delete an advocate




@api_view(['GET'])
def endpoints(request):
    data = ['/advocate_list', '/advocate_detail/:username']
    return Response(data)


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def advocate_list(request):
    if request.method == 'GET':
        # Handles GET requests
        query = request.GET.get('query')

        if query is None:
            query = ""

        advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
        serializer = AdvocateSerializer(advocates, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        username = request.data['username']
        bio = request.data['bio']
        print(username, bio)
        advocate = Advocate.objects.create(username=request.data['username'], bio=request.data['bio'])
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)






@api_view(['GET', 'PUT', 'DELETE'])
def advocate_detail(request, username):
    advocate = Advocate.objects.get(username=username)

    if request.method == 'GET':
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        advocate.username = request.data['username']
        advocate.bio = request.data['bio']
        advocate.save()
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)


    if request.method == 'DELETE':
        if advocate is not None:
            advocate.delete()
            print('success')
            return Response('user was deleted')


@api_view(['GET'])
def companies_list(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)



