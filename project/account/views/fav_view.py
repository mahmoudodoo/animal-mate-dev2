from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from ..models import Account
from animal.models import AnimalImage

@login_required  
def profile_fav_cats(request):
    user = request.user
    favorite_animals = user.favorite_animals.all()
    fav_animals = []
    for animal in favorite_animals:
        animal_images = AnimalImage.objects.filter(animal=animal.id).all()
        fav_animals.append({
            'id':animal.id,
            'name':animal.name,
            'image_1':animal_images[0].image,
            'image_2':animal_images[1].image,
            'image_3':animal_images[2].image,
        })
    context = {
        'favorite_animals': fav_animals,
    }
    
    return render(request, 'profile_fav_cats.html', context)


def delete_favorite_animal(request,animal_id):
    if request.method == 'POST':
        user = request.user
        animal_to_remove = user.favorite_animals.get(id=animal_id)
        user.favorite_animals.remove(animal_to_remove)
            
    favorite_animals = user.favorite_animals.all()
    context = {
    'favorite_animals': favorite_animals,
    }
    return render(request, 'update_fav_data.html', context)