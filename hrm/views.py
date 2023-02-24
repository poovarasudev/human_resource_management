from ajax_datatable import AjaxDatatableView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView
from django.urls import reverse, reverse_lazy

from core import template_utils
from hrm.forms import EmployeeForm
from hrm.models import Employee


# Create your views here.


@login_required()
def dashboard(request):
    return render(request, 'dashboard.html')


class EmployeeList(LoginRequiredMixin, TemplateView):
    template_name = 'employees/index.html'


class EmployeeAjaxDatatableView(LoginRequiredMixin, AjaxDatatableView):
    model = Employee
    initial_order = [['name', 'asc']]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'All']]
    search_values_separator = '+'
    column_defs = [
        {'name': 'id', 'visible': False, 'searchable': False},
        {'name': 'name', 'visible': True},
        {'name': 'mobile_number', 'visible': True},
        {'name': 'aadhaar_number', 'visible': True},
        {'name': 'job_type', 'visible': True, 'choices': Employee.JOB_TYPES},
        {'name': 'employee_type', 'visible': True, 'choices': Employee.EMPLOYEE_TYPES},
        {'name': 'action', 'title': 'Action', 'visible': True, 'searchable': False, 'orderable': False, 'className': 'text-center'},
    ]

    def customize_row(self, row, obj):
        buttons = template_utils.show_button(reverse("employees.detail", args=[obj.id])) \
                  + template_utils.edit_button(reverse("employees.edit", args=[obj.id])) \
                  + template_utils.delete_button(reverse("employees.delete", args=[obj.id]), obj.name)
        row['action'] = f'<div class="form-inline justify-content-center">{buttons}</div>'
        return


class EmployeeCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Employee
    template_name = 'employees/form.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('employees')
    success_message = 'Employee created successfully.'


class EmployeeUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Employee
    template_name = 'employees/form.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('employees')
    success_message = 'Employee updated successfully.'


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = 'employees/show.html'


@require_http_methods(['DELETE'])
@login_required()
def delete_employee(request, pk):
    try:
        employee = get_object_or_404(Employee, id=pk)
        # TODO :: Need to implement softdelete
        employee.delete()
        return JsonResponse({'message': 'Employee deleted successfully'})
    except Exception as e:
        return JsonResponse({'message': 'Error while deleting Employee!'}, status=500)

