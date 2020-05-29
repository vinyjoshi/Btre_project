from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        # Check if already made an enquiry:
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'Enquiry already made for this Property!')
                return redirect('/listings/'+listing_id)

        Contact.objects.create(listing_id=listing_id, listing=listing, user_id=user_id,
                name=name, email=email, phone=phone, message=message).save()
        
        # Send E-mail:
        send_mail(
            'Property Listing Enquiry',
           'There has been an inquiry for {}. Sign into the admin panel for more info.'.format(listing),
            'viyj1995@gmail.com',
            [realtor_email, 'viyj2000@gmail.com'],
            fail_silently=False
        )
        
        messages.success(request,'Your request has been submitted. A realtor will get back to you soon.')
        return redirect('/listings/'+listing_id)