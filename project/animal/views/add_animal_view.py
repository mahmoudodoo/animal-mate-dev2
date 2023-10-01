import os
import pandas as pd
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render, redirect
from ..models import Animal,AnimalImage
from django.contrib import messages
import uuid
from django.contrib.auth.decorators import login_required

# Construct the absolute path to your CSV file using the BASE_DIR setting
csv_file_path = os.path.join(settings.BASE_DIR, 'static/data/cities.csv')
# Load the CSV data into a Pandas DataFrame
data = pd.read_csv(csv_file_path)

@login_required
def add_animal(request):
    if request.method == 'POST':
        # Handle the form submission
        name = request.POST.get('name')
        birth_day = request.POST.get('birth_day')
        gender = request.POST.get('gender')
        country = request.POST.get('country_animal')
        city = request.POST.get('city')
        categ = request.POST.get('categ')
        price = request.POST.get('price')
        user = request.user

        # Create a new Animal object
        animal = Animal(
            name=name,
            birth_day=birth_day,
            gender=gender,
            country=country,
            city=city,
            categ=categ,
            price=price,
            user=user,
        )

        # Save the Animal object
        animal.save()

        for uploaded_file in request.FILES.getlist('file-input2'):
            # Get the original file extension
            file_extension = os.path.splitext(uploaded_file.name)[-1]
            
            # Generate a unique filename using UUID with the original file extension
            filename = f'{uuid.uuid4()}{file_extension}'
            
            # Create an AnimalImage object with the new filename
            animal_image = AnimalImage(animal=animal, image=uploaded_file)
            animal_image.image.name = filename  # Set the new filename
            animal_image.save()

        messages.success(request, 'Animal added successfully')
        return redirect('add_animal')
    return render(request, 'add_animal.html')




def get_cities(request):
    selected_country = request.GET.get('selected_country')
    filtered_cities = data[data['country_name'] == selected_country]['name'].tolist()
    return JsonResponse({'cities': filtered_cities})