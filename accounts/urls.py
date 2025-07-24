from django.urls import path
from accounts.views.accounts.DashboardView import DashboardView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
]
