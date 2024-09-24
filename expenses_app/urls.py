from django.urls import path

from .views import ExpensesListCreateView, ExpenseRetrieveUpdateDestroyView

urlpatterns = [
    path('expenses/' , ExpensesListCreateView.as_view(), name='expense-list-create'),
    path('expenses/<int:pk>/', ExpenseRetrieveUpdateDestroyView.as_view(), name='expense-detail'),
]
