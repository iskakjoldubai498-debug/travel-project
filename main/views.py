import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Tour

# 1. Башкы бет (Бул жерде index функциясы сөзсүз болушу керек!)
def index(request):
    tours = Tour.objects.filter(is_active=True)[:6] # Эң акыркы 6 турду чыгаруу
    return render(request, 'main/index.html', {'tours': tours})

# 2. Биз жөнүндө
def about(request):
    return render(request, 'main/about.html')

# 3. Байланыш
def contact(request):
    return render(request, 'main/contact.html')

# 4. Турлардын тизмеси
def tours_list(request):
    tours = Tour.objects.filter(is_active=True)
    return render(request, 'main/tours.html', {'tours': tours})

# 5. Турдун толук маалыматы
def tour_detail(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    return render(request, 'main/tour_detail.html', {'tour': tour})

# 6. Telegram бот аркылуу заказ кабыл алуу
# 6. Telegram бот аркылуу заказ кабыл алуу
def callback_request(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')

        token = "8632706293:AAGUFr-eBHri8U9BLUZ_5j19g9flYnmngqw" # Бул жерге өз токениңизди коюңуз
        chat_id = "6365816184"
        text = f"🚀 *ЖАҢЫ ЗАКАЗ!*\n\n👤 *Аты:* {name}\n📞 *Тел:* {phone}"

        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}

        try:
            response = requests.post(url, data=data, timeout=5)
            if response.status_code == 200:
                messages.success(request, "Биз сиздин билдирүүнү алдык! Тез арада байланышабыз.")
            else:
                messages.error(request, "Байланышта ката кетти (Telegram error).")
        except requests.exceptions.RequestException:
            messages.error(request, "Интернет байланышы үзүлдү.")

    return redirect('index')

from django.shortcuts import render
from .models import Tour  # Сиз түзгөн моделди чакырабыз

def index(request):
    tours = Tour.objects.all()  # Базадагы бардык турларды алабыз
    return render(request, 'main/index.html', {'tours': tours})


import hashlib
from django.shortcuts import redirect, get_object_or_404

def create_payment(request, tour_id):
    # Төлөмдү түзүү логикасы бул жерде болот...
    # Азырынча тест катары бир жерге redirect кылып турсаңыз болот
    from django.shortcuts import redirect
    return redirect('index') # Же төлөм системасына багыттоо


import hashlib
from django.shortcuts import render, get_object_or_404, redirect
from .models import Tour, Order


def create_payment(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)

    # 1. Базада заказды түзөбүз
    order = Order.objects.create(
        tour=tour,
        amount=tour.price,
        full_name=request.user.username if request.user.is_authenticated else "Аноним"
    )

    # 2. PayBox параметрлери (Бул жерге өзүңүздүн ID'лерди коюңуз)
    merchant_id = '555555'  # Сиздин чыныгы Merchant ID
    secret_key = 'your_secret_key'  # Сиздин жашыруун ачкычыңыз
    salt = 'random_string_123'

    params = {
        'pg_merchant_id': merchant_id,
        'pg_amount': str(int(tour.price)),
        'pg_currency': 'KGS',
        'pg_order_id': str(order.id),
        'pg_description': f'Тур: {tour.title}',
        'pg_salt': salt,
    }

    # 3. Коопсуздук үчүн электрондук кол тамга (Signature) түзүү
    # Параметрлерди алфавит тартибинде тизип, жашыруун ачкыч менен аралаштырабыз
    sorted_params = sorted(params.items())
    param_values = [str(v) for k, v in sorted_params]
    sig_str = 'payment.php;' + ';'.join(param_values) + ';' + secret_key
    signature = hashlib.md5(sig_str.encode()).hexdigest()

    params['pg_sig'] = signature

    # 4. Банктын төлөм барагына багыттоо
    query_string = '&'.join([f"{k}={v}" for k, v in params.items()])
    payment_url = f"https://api.paybox.money/payment.php?{query_string}"

    return redirect(payment_url)
from django.shortcuts import render, get_object_or_404
from .models import Tour

def index(request):
    tours = Tour.objects.all()[:3] # Башкы бетке болгону 3 тур чыгарабыз
    return render(request, 'main/index.html', {'tours': tours})
def tours(request):
    tours = Tour.objects.all()  # Базадагы бардык турларды алат
    return render(request, 'main/tours.html', {'tours': tours})
def tour_detail(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    return render(request, 'main/tour_detail.html', {'tour': tour})

def about(request):
    return render(request, 'main/about.html')
def about(request): # Сиздин urls.py'да 'about' деп аталгандыктан ушундай жаздык
    return render(request, 'main/contact.html') # Бул жерде файлдын аты туура болушу шарт!


from django.shortcuts import render
from .models import Tour
from django.db.models import Q


def index(request):
    # 'search_word' - бул HTML формадагы input'тун аталышы
    query = request.GET.get('search_word')

    if query:
        # Аталышы же маалыматы боюнча издөө (чоң-кичине тамганы айырмалабайт)
        tours = Tour.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        # Издөө жок болсо, акыркы кошулган 6 турду көрсөтөбүз
        tours = Tour.objects.all().order_by('-id')[:6]

    context = {
        'tours': tours,
        'query': query,
    }
    return render(request, 'main/index.html', context)


from django.shortcuts import render
from .models import Tour
from django.db.models import Q


def index(request):
    query = request.GET.get('search_word')

    if query:
        # Издөө тексти болсо, чектөөсүз баарын издейт
        tours = Tour.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        # Издөө жок болсо, болгону 3 турду гана алат
        tours = Tour.objects.all().order_by('-id')[:3]

    return render(request, 'main/index.html', {'tours': tours, 'query': query})


from django.db.models import Q


def index(request):
    query = request.GET.get('search_word', '').strip()  # strip() ашыкча боштуктарды алат

    if query:
        # Сөздөрдү бөлүп алуу (мисалы: "Көл Ысык" деп жазса да табуу үчүн)
        search_words = query.split()

        # Баштапкы суроо: баарын издөө
        tours = Tour.objects.all()

        for word in search_words:
            # Ар бир сөздү өз-өзүнчө текшерет (Атынан же Сүрөттөмөсүнөн)
            tours = tours.filter(
                Q(title__icontains=word) |
                Q(description__icontains=word)
            )
    else:
        # Эгер издөө жок болсо, 3 популярдуу тур
        tours = Tour.objects.all().order_by('-id')[:3]

    return render(request, 'main/index.html', {'tours': tours, 'query': query})


from django.http import JsonResponse
from .models import Tour


def tour_autocomplete(request):
    query = request.GET.get('term', '')  # JavaScript'тен келген текст
    tours = Tour.objects.filter(title__icontains=query)[:4]  # Болгону 4 вариант

    results = []
    for tour in tours:
        results.append({
            'id': tour.id,
            'title': tour.title,
            # 'url': tour.get_absolute_url() # Эгер сизде бул функция болсо
        })

    return JsonResponse(results, safe=False)


from django.http import JsonResponse
from .models import Tour
from django.db.models import Q


# Autocomplete үчүн өзүнчө View
def tour_autocomplete(request):
    query = request.GET.get('term', '')  # JavaScript'тен 'term' катары келет
    if query:
        # Аталышында ошол тамгалар бар 4 турду табабыз
        tours = Tour.objects.filter(title__icontains=query)[:4]
        results = []
        for tour in tours:
            results.append({
                'id': tour.id,
                'title': tour.title
            })
        return JsonResponse(results, safe=False)
    return JsonResponse([], safe=False)


# Башкы беттин негизги View функциясы
def index(request):
    query = request.GET.get('search_word', '').strip()
    if query:
        tours = Tour.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    else:
        tours = Tour.objects.all().order_by('-id')[:3]

    return render(request, 'main/index.html', {'tours': tours, 'query': query})