from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            messages.success(request, 'Сообщение успешно отправлено!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def special_offer_view(request):
    messages.add_message(request, 60, 'Специальное предложение для VIP-пользователей!')
    return render(request, 'special_offer.html')

def home(request):
    return render(request, 'home.html')