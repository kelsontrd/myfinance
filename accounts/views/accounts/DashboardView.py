from django.shortcuts import render, HttpResponse
from django.views import View

class DashboardView(View):
    def get(self, request):
        return HttpResponse("Welcome to the Dashboard!")