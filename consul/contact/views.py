from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
# si todo va bien  redireccional
            email = EmailMessage(
                "De CRIM: Nuevo mensaje de contacto", #asunto
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),   #cuerpo
               # "no-contestar@inbox.google.com",    #email_origen
                "no-contestar@inbox.mailtrap.io",
                ["znup.kreyz.vlc@gmail.com"],    #email_destino
                reply_to=[email]
            )
            try:
                email.send()
                #Todo va bien
                return redirect(reverse('contact')+"?ok")
            except:
                #algo va mal
                return redirect(reverse('contact')+"?Fail")

    return render(request,"contact/contact.html", {'form':contact_form})