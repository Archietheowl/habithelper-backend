from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from utils.exceptions import handle_exceptions
from .models import Habit_Helper

# Create your views here.


class ListCreateHabit_HelperView(APIView):

    # Index Controller
    # GET /habit_helpers/
    @handle_exceptions
    def get(self, request):

        return Response('HIT INDEX ROUTE')

    # Create Controller
    # POST /habit_helpers/
    @handle_exceptions
    def post(self, request):

        return Response('HIT CREAT ROUTE')


class RetrieveUpdateDestroyHabit_HelperView(APIView):

    # Show Controller
    # GET /habit_helpers/:pk/
    @handle_exceptions
    def get(self, request, pk):

        return Response('HIT SHOW ROUTE')

    # Delete Controller
    # DELETE /habit_helpers/:pk/

    @handle_exceptions
    def delete(self, request, pk):

        return Response('HIT DELETE ROUTE')

    # Update Controller
    # PUT /habit_helpers/:pk/
    @handle_exceptions
    def put(self, request, pk):

        return Response('HIT UPDATE ROUTE')
