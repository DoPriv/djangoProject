from django.shortcuts import render


# Create your views here.

def start_page(request):
    return render(request, 'start_page.html')


def about_us(request):
    return render(request, 'about_us.html')


def our_service(request):
    return render(request, 'our_service_template.html')
