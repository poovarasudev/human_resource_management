from django import forms


from .models import Employee


class EmployeeForm(forms.ModelForm):
    mobile_number = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Mobile No...',
            }
        ),
        min_length=10,
        max_length=10,
    )
    aadhaar_number = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Aadhaar No...',
            }
        ),
        min_length=12,
        max_length=12,
    )

    class Meta:
        model = Employee
        fields = ('name', 'mobile_number', 'aadhaar_number', 'address', 'job_type', 'employee_type')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name...'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address...'}),
            'job_type': forms.Select(attrs={'class': 'form-control select2', 'placeholder': 'Job Type...'}),
            'employee_type': forms.Select(attrs={'class': 'form-control select2', 'placeholder': 'Employee Type...'}),
        }
