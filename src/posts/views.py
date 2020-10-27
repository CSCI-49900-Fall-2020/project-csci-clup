from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.shortcuts import render, redirect
from .models import Post
from .forms import CustomerSignUpForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string

from posts.forms import CustomerSignUpForm

# from mysite.core.forms import SignUpForm

# Create your views here.

#CRUD Create Retrieve Update Delete

#List all the posts 

def base_view(request, *args, **kwargs):
    return render(request, "base.html", {})

def home_page_view(request,*args, **kwargs):
    print(request)
    print(request.user)
    return render(request, "home_page.html", {})

def contact_page_view(request, *args, **kwargs):

    return render(request, "contact_us.html", {})

def about_us_page_view(request,*args, **kwargs):
     return render(request, "about_us.html", {})

def about_us_page_view(request,*args, **kwargs):
    return render(request, "about_us.html", {})

def signup_signin_page_view(request, *args, **kwargs):
    return render(request, "signin.html", {})

<<<<<<< HEAD
=======

def signout_page_view(request):
    if request.method == "POST":
        logout(request)
        return render(request, "home_page.html", {})


@login_excluded(home_page_view)
def forgot_password_view(request, *args, **kwargs):
	return render(request, "reset.html", {})


@user_must_login(please_login_view)
def control_panel_view(request, *args, **kwargs):
    return render(request, "control_panel.html", {})


@user_must_login(please_login_view)
def profile_setting_view(request, *args, **kwargs):
    obj=Business.objects.all().filter(username = request.user.get_username())
    if request.method == 'POST':
        obj.update(first_name = request.POST.get('first_name')),
        obj.update(last_name= request.POST.get('last_name')), 
        obj.update(email= request.POST.get('email')),
        obj.update(phone_number = request.POST.get('phone_number')),
        obj.update(store_name = request.POST.get('store_name')),
        obj.update(store_number = request.POST.get('store_number')),
        obj.update(store_address = request.POST.get('store_address')),
        obj.update(city = request.POST.get('city')),
        obj.update(state = request.POST.get('state')),
        obj.update(zipcode = request.POST.get('zipcode')),
        obj.update(input_sex = request.POST.get('input_sex')),
        obj.update(sunday_open = request.POST.get('sunday_open')),
        obj.update(sunday_closed = request.POST.get('sunday_closed')),
        obj.update(monday_open = request.POST.get('monday_open')),
        obj.update(monday_closed = request.POST.get('monday_closed')),
        obj.update(tuesday_open = request.POST.get('tuesday_open')),
        obj.update(tuesday_closed = request.POST.get('tuesday_closed')),
        obj.update(wednesday_open = request.POST.get('wednesday_open')),
        obj.update(wednesday_closed = request.POST.get('wednesday_closed')),
        obj.update(thursday_open = request.POST.get('thursday_open')),
        obj.update(thursday_closed = request.POST.get('thursday_closed')),
        obj.update(friday_open = request.POST.get('friday_open')),
        obj.update(friday_closed = request.POST.get('friday_closed')),
        obj.update(saturday_open = request.POST.get('saturday_open')),
        obj.update(saturday_closed = request.POST.get('saturday_closed')),
        for item in obj:
            item.save()
    obj=Business.objects.all().filter(username = request.user.get_username())
    return render(request, "profile_setting.html", {'obj': obj})


@login_excluded(home_page_view)
def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Line Up',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'david.chen68@myhunter.cuny.edu', [user.email], fail_silently=False)
					except BadHeaderError:

						return HttpResponse('Invalid header found.')
						
					messages.success(request, 'A message with the reset password instructions has been sent to your inbox.')
					return redirect ("/password_reset/done/")
			messages.error(request, 'An invalid email has been entered.')
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})

@login_excluded(home_page_view)
>>>>>>> parent of 5b4016ae... Removed input sex
def customer_signup_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.cell_number = form.cleaned_data.get('cell_number')
            user.save()
            user.refresh_from_db()
            # user_username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return render(request, "home_page.html", {})
            # return redirect(home_page_view)
        else: 
            print("here")
            print(form.errors)  
    else:
        form = CustomerSignUpForm()
    return render(request, "signup.html", {'form': form})

def business_signup_view(request, *args, **kwargs):
<<<<<<< HEAD
=======
    if request.method == 'POST'and request.POST['action'] == 'Business':
        form = BusinessSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            #Save to profiles
            user.refresh_from_db()
            user.profile.username = form.cleaned_data.get('username')
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.phone_number = form.cleaned_data.get('phone_number')
            user.profile.is_business = True
            user.save()
            # #Save to db
            business = Business.objects.create(
                first_name = request.POST.get('first_name'),
                last_name= request.POST.get('last_name'), 
                email= request.POST.get('email'),
                phone_number = request.POST.get('phone_number'),
                store_name = request.POST.get('store_name'),
                store_number = request.POST.get('store_number'),
                store_address = request.POST.get('store_address'),
                city = request.POST.get('city'),
                state = request.POST.get('state'),
                zipcode = request.POST.get('zipcode'),
                input_sex = request.POST.get('input_sex')
                )
            raw_password = form.cleaned_data.get('password1')
            business = authenticate(username=user.username, password=raw_password)
            login(request, business)
            return redirect(home_page_view)
        else: 
            print(form.errors)
    else:
        form = BusinessSignUpForm()
        return render(request, 'b_signup.html', {'form': form})
>>>>>>> parent of 5b4016ae... Removed input sex
    return render(request, "b_signup.html", {})

def business_login_view(request, *args, **kwargs):
	return render(request, "b_login.html", {})

def forgot_password_view(request, *args, **kwargs):
	return render(request, "reset.html", {})

def control_panel_view(request, *args, **kwargs):
    return render(request, "control_panel.html", {})

def profile_setting_view(request, *args, **kwargs):
    return render(request, "profile_setting.html", {})

def customer_control_view(request, *args, **kwargs):
    return render(request, "customer_control.html", {})

def customer_profile_view(request, *args, **kwargs):
    return render(request, "customer_profile.html", {})

def scheduled_view(request, *args, **kwargs):
    return render(request, "scheduled.html", {})