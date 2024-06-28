from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import CustomUser
from django.contrib.admin.views.decorators import staff_member_required

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user.is_student:
                login(request, user)
                return redirect('student_dashboard')
            elif user.is_lecturer:
                return redirect('pending_approval')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_student:
                return redirect('student_dashboard')
            elif user.is_lecturer and user.is_approved:
                return redirect('lecturer_dashboard')
            elif user.is_lecturer:
                return redirect('pending_approval')
            elif user.is_superuser:
                return redirect('admin_dashboard')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

@staff_member_required
def approve_lecturer(request):
    lecturers = CustomUser.objects.filter(is_lecturer=True, is_approved=False)
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = CustomUser.objects.get(id=user_id)
        user.is_approved = True
        user.save()
    return render(request, 'approve_lecturer.html', {'lecturers': lecturers})

def pending_approval(request):
    return render(request, 'pending_approval.html')
