from django.shortcuts import render, redirect
from ..models import Account
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def profile_edit(request):
    # Assuming you have a user profile associated with the current user
    user_profile = request.user 

    context = {
        'user_profile': user_profile,
    }

    return render(request, 'profile_edit.html', context)


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_profile = request.user  # Access the current user

        # Convert the string "true" to the boolean True
        activate_whatsapp = request.POST.get('activate_whatsapp', False)
        if activate_whatsapp == 'true':
            activate_whatsapp = True
        else:
            activate_whatsapp = False

        # Update user_profile fields with the data from the form
        user_profile.full_name = request.POST.get('full_name')
        user_profile.username = request.POST.get('username')
        user_profile.mobile_number = request.POST.get('mobile')
        user_profile.activate_whatsapp = activate_whatsapp
        user_profile.email = request.POST.get('email')
        # Update other fields as needed

        user_profile.save()
        messages.success(request, 'Profile updated successfully')
        return redirect('profile_edit')
    else:
        messages.error(request, 'Invalid request method')
        return redirect('profile_edit')
    
@login_required
def upload_profile_image(request):
    if request.method == 'POST':
        user_profile = request.user  # Access the current user

        # Handle the profile image upload
        profile_image = request.FILES.get('profile_image')
        if profile_image:
            # Check if the current profile image is not the default 'avatar.jpg'
            if user_profile.profile_image.name != 'profile_images/avatar.jpg':
                # Remove the old profile image, if it exists and it's not 'avatar.jpg'
                if user_profile.profile_image:
                    user_profile.profile_image.delete(save=False)

            # Save the new profile image
            user_profile.profile_image = profile_image
            user_profile.save()

            messages.success(request, 'Profile image updated successfully')
        else:
            messages.error(request, 'No image selected')

        return redirect('profile_edit')
    else:
        messages.error(request, 'Invalid request method')
        return redirect('profile_edit')
    

@login_required
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        user = request.user

        if user.check_password(old_password):
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)  # Update session with new password
                messages.success(request, 'Password updated successfully.')
                return JsonResponse({'success': True})
            else:
                messages.error(request, 'New passwords do not match.')
                return JsonResponse({'success': False, 'error_message': 'New passwords do not match.'})
        else:
            messages.error(request, 'Old password is incorrect.')
            return JsonResponse({'success': False, 'error_message': 'Old password is incorrect.'})
    return redirect('profile_edit')