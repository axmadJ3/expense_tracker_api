from rest_framework import generics, permissions
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta

from .models import Expense
from .serializers import ExpenseSerializer


class ExpensesListCreateView(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        queryset = Expense.objects.filter(user=user)
        
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')
        if date_from and date_to:
            queryset = queryset.filter(date__range=[date_from, date_to])
        elif 'otgan_hafta' in self.request.query_params:
            last_week = timezone.now() - timedelta(days=7)
            queryset = queryset.filter(date__gte=last_week)
        elif 'otgan_oy' in self.request.query_params:
            last_month = timezone.now() - timedelta(days=30)
            queryset = queryset.filter(date__gte=last_month)
        elif 'otgan_3_oy' in self.request.query_params:
            last_three_months = timezone.now() - timedelta(days=90)
            queryset = queryset.filter(date__gte=last_three_months)
        
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

class ExpenseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)
    