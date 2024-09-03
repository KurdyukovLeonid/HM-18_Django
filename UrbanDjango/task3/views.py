from django.shortcuts import render

# Create your views here.
def platform(request):
    return render(request, 'third_task/platform.html')

def games(request):
    items = {
        'Atomic Heart': '2000 р.',
        'Cyberpunk 2077': '2500 р.',
        'Payday 2': '1000 р.',
    }
    return render(request, 'third_task/games.html', {'items': items})

def cart(request):
    return render(request, 'third_task/cart.html')
