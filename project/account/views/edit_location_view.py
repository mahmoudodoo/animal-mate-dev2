# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def edit_location(request):
    if request.method == 'POST':
        # Get the location data from the form submission
        location_data = request.POST.get('location', '')
        
        # Perform any necessary data validation here

        # Update the user's location field
        request.user.location = location_data
        request.user.save()

        # Display a success message
        messages.success(request, 'Location updated successfully.')

        return redirect('edit_location')  # Redirect back to the edit_location page

    return render(request, 'edit_location.html')
