from django.shortcuts import render, redirect
from django.shortcuts import render
from .forms import ContactForm





def home(request):
    return render(request, 'home.html')




def contact_view(request):
    success = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()   # <--- Esto guarda DIRECTO en la base de datos
            success = True
            form = ContactForm()  # Limpia el form

    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form, "success": success})
