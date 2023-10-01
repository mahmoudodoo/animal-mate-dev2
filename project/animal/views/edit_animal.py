import os
import uuid
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Animal, AnimalImage
from django.contrib.auth.decorators import login_required

@login_required
def edit_animal(request, animal_id):
    # Fetch the existing Animal object
    animal_object = Animal.objects.filter(id=animal_id).first()
    print(request.path)
    if request.method == 'POST':
        # Update the fields in the Animal object based on the form data
        animal_object.name = request.POST.get('name')
        animal_object.birth_day = request.POST.get('birth_day')
        animal_object.gender = request.POST.get('gender')
        animal_object.country = request.POST.get('country_animal')
        animal_object.city = request.POST.get('city_form')
        animal_object.categ = request.POST.get('categ')
        animal_object.price = request.POST.get('price')

        # Save the updated Animal object
        animal_object.save()

        # Handle image uploads and updates
        image_1 = request.FILES.get('image_1')
        image_2 = request.FILES.get('image_2')
        image_3 = request.FILES.get('image_3')
        image_4 = request.FILES.get('image_4')

        image_fields = [image_1, image_2, image_3, image_4]

        for index, uploaded_image in enumerate(image_fields):
            if uploaded_image:
                # Generate a unique filename for the uploaded image using UUID
                unique_filename = f'{uuid.uuid4().hex}{os.path.splitext(uploaded_image.name)[1]}'

                # Get the corresponding AnimalImage object (order is 0-based)
                animal_image = AnimalImage.objects.filter(animal=animal_object)[index]

                # Remove the existing image file if it exists
                if animal_image and animal_image.image:
                    old_image_path = os.path.join(settings.MEDIA_ROOT, str(animal_image.image))
                    if os.path.exists(old_image_path):
                        os.remove(old_image_path)

                # Update the image path in the AnimalImage model
                animal_image.image = f"animal_images/{unique_filename}"
                animal_image.save()

                # Save the uploaded image with the generated filename
                image_path = os.path.join(settings.MEDIA_ROOT, 'animal_images', unique_filename)
                with open(image_path, 'wb+') as destination:
                    for chunk in uploaded_image.chunks():
                        destination.write(chunk)

        messages.success(request, 'Animal details updated successfully.')
        return redirect('edit_animal', animal_id=animal_object.id)

    animal_images = AnimalImage.objects.filter(animal=animal_object).all()
    images = {
        'image_1': None,
        'image_2': None,
        'image_3': None,
        'image_4': None,
    }

    # Check if there are images and assign them if available
    if animal_images:
        for i, animal_image in enumerate(animal_images[:4]):
            images[f'image_{i + 1}'] = animal_image.image

    animal = {
        'id': animal_object.id,
        'name': animal_object.name,
        'birth_day': animal_object.birth_day,
        'gender': animal_object.gender,
        'country': animal_object.country,
        'city': animal_object.city,
        'categ': animal_object.categ,
        'price': animal_object.price,
        'user': animal_object.user,
        'images': images,
    }

    context = {
        'animal': animal,
    }
    return render(request, 'edit_animal.html', context=context)
