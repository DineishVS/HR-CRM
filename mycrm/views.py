from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import Record, CsvFile

import csv
# @login_required
# def upload_csv(request):
#     if request.method == 'POST':
#         form = SignForm(request.POST, request.FILES)
#         if form.is_valid():
#             csv_file = request.FILES['file']
#             if not csv_file.name.endswith('.csv'):
#                 messages.error(request, 'This is not a CSV file')
#                 return redirect('upload_csv')
#             # Read the CSV file
#             decoded_file = csv_file.read().decode('utf-8').splitlines()
#             reader = csv.reader(decoded_file)
#             next(reader)  # Skip the header row
#             for row in reader:
#                 Record.objects.create(
#                     first_name=row[0],
#                     last_name=row[1],
#                     email=row[2],
#                     phone_number=row[3],
#                     city=row[4],
#                     state=row[5]
#                 )
#             messages.success(request, 'CSV file uploaded successfully')
#             return redirect('home')
#     else:
#         form = SignForm()
#     return render(request, 'upload_csv.html', {'form': form})
def home_view(request):
    records = Record.objects.all()
    return render(request, 'home.html', {'records': records})

def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registered successfully')
            return redirect('home')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = SignForm()

    return render(request, 'register.html', {'form': form})

def employee_record(request, id):  # Ensure 'id' is in the function signature
    if request.user.is_authenticated:
        employee_record = get_object_or_404(Record, id=id)
        return render(request, 'employee_record.html', {'employee_record': employee_record})
    else:
        messages.error(request, 'You must be logged in to view this page.')
        return redirect('login')

def add_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Assuming 'home' is the name of your home URL pattern
    else:
        form = RecordForm()
    return render(request, 'addrecord.html', {'form': form})
def delete_record(request, id):

    delete_record = get_object_or_404(Record, id=id)

    delete_record.delete()
    messages.success(request, 'Record deleted successfully.')
    return redirect('home')


def update_record(request, id):
    record = get_object_or_404(Record, id=id)

    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record updated successfully.')
            return redirect('home')  # Redirect to home or any other view
    else:
        form = RecordForm(instance=record)

    return render(request, 'update_record.html', {'record': record, 'form': form})
def upload_csv(request):
    if request.method == 'POST':
        form = CsvFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_instance = form.save(commit=False)
            csv_instance.user = request.user  # Assuming user is authenticated
            csv_instance.save()
            # Process the uploaded CSV file
            handle_uploaded_csv(csv_instance.csv_file.path)
            return redirect('display_csv', pk=csv_instance.pk)  # Redirect to display CSV contents
    else:
        form = CsvFileForm()
    return render(request, 'upload_csv.html', {'form': form})

def handle_uploaded_csv(file_path):
    # Example function to handle processing of uploaded CSV file
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Process each row as needed
            print(row)  # Example: Print each row to console

def display_csv(request, pk):
    csv_instance = CsvFile.objects.get(pk=pk)
    with open(csv_instance.csv_file.path, 'r') as file:
        reader = csv.reader(file)
        csv_data = list(reader)
    return render(request, 'display_csv.html', {'csv_data': csv_data})