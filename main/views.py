import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Tour
from django.db.models import Q

# 1. Башкы бет
def index(request):
    query = request.GET.get('search_word', '').strip()
    if query:
        tours = Tour.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    else:
        tours = Tour.objects.filter(is_active=True).order_by('-id')[:6]
    return render(request, 'main/index.html', {'tours': tours, 'query': query})

# 2. ТУРЛАР БЕТИ (Ката ушул жерден чыгып жаткан)
def tours(request):
    tours = Tour.objects.all()  # Же башка бар болгон талаа менен фильтрлеңиз
    return render(request, 'main/tours.html', {'tours': tours})

# 3. Биз жөнүндө
def about(request):
    return render(request, 'main/about.html')

# 4. Байланыш
def contact(request):
    return render(request, 'main/contact.html')

# 5. Турдун толук маалыматы
def tour_detail(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    return render(request, 'main/tour_detail.html', {'tour': tour})

# 6. Бот
def callback_request(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        token = "8632706293:AAGUFr-eBHri8U9BLUZ_5j19g9flYnmngqw"
        chat_id = "6365816184"
        text = f"🚀 ЖАҢЫ ЗАКАЗ!\n👤 Аты: {name}\n📞 Тел: {phone}"
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        try:
            requests.post(url, data={"chat_id": chat_id, "text": text}, timeout=5)
            messages.success(request, "Билдирүү кетти!")
        except:
            messages.error(request, "Ката!")
    return redirect('index')