from django.urls import path

from . import views


urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),

    # Employees CRUD
    path('employees', views.EmployeeList.as_view(), name='employees'),
    path('employees-datatable', views.EmployeeAjaxDatatableView.as_view(), name='employees.datatable'),
    path('employees/create', views.EmployeeCreateView.as_view(), name='employees.create'),
    path('employees/<int:pk>', views.EmployeeDetailView.as_view(), name='employees.detail'),
    path('employees/<int:pk>/edit', views.EmployeeUpdateView.as_view(), name='employees.edit'),
    path('employees/<int:pk>/delete', views.delete_employee, name='employees.delete'),
]

