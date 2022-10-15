from email.message import EmailMessage

from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
# Create your views here.
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import Generate_Token


def ho(request):
    return render(request, "hello.html")


def order(request):
    return render(request, "order.html")


def About(request):
    return render(request, "About.html")


def con(request):
    return render(request, "contact.html")


def sign(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        mobileno = request.POST.get("mobileno")
        myuser = User.objects.create_user(username, email, password)
        myuser.is_active = True
        myuser.mobileno = mobileno

        if not username.isalnum():
            messages.error(request, "User name must be alpha numeric")

        myuser.save()
        messages.success(request,
                         "Your account has been successfully created we have sent you a confirmation email!please confirm your email to activate your account")

        subject = "Welcome to Aaharam"
        message = "Hello!" + myuser.username + "! \n\n" + "Welcome to Aaharam!\n\nThankyou for registering for our website \n\n we have also sent you a confirmation email ,please confirm your email address in order to activate your account\n\n" + "Thanking you\n\n Bhuvana"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        current_site = get_current_site(request)
        email_subject = "Confirm your email for Aaharam website"
        message2 = render_to_string('email_confirmation.html', {
            'name': myuser.username,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': Generate_Token.make_token(myuser)

        })
        email = EmailMessage(email_subject, message2, settings.EMAIL_HOST_USER, [myuser.email], )
        email.fail_silently = True
        email.send()

        return redirect("home")
    return render(request, "signup.html")


def home(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in succesfully")
            return render(request, "hello.html", {})
        else:
            return HttpResponse("<h1>Wrong credentials check again!</h1>")

    return render(request, "lo.html")


def activate(request, uid64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        myuser = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and Generate_Token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        # login(myuser,request)
        return redirect('home')
    else:
        return render(request, 'activation_failed.html')


def orderin(request):
    return render(request, 'orderin1.html')


def orderin2(request):
    return render(request, 'orderin2.html')


def orderin3(request):
    return render(request, 'orderin3.html')


def orderin4(request):
    return render(request, 'orderin4.html')


def orderin5(request):
    return render(request, 'orderin5.html')


def orderin6(request):
    return render(request, 'orderin6.html')

def cart(request):
    return render(request, 'cart.html')
