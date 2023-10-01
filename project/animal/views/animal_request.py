from django.shortcuts import render
from ..models import AnimalRequest,Animal
from django.contrib.auth.decorators import login_required

@login_required
def animal_requasts(request):
    animals = Animal.objects.filter(user=request.user).all()
    
    animal_requests =[]
    if animals:
        for animal in animals:
            animal_request = AnimalRequest.objects.filter(animal=animal).first()
            if animal_request:
                animal_requests.append(
                    {
                        "name":animal_request.cat_name(),
                        "status":animal_request.status,
                        "user":animal_request.user_cat(),
                        "birth_day":animal_request.birth_day(),
                        "city":animal_request.cat_city(),
                        "price":animal_request.cat_price()
                    }
                )

    context = {
        "animal_requests":animal_requests,
    }
    return render(request, 'animal_requasts.html',context=context)