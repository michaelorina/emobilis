from django.shortcuts import render

# Create your views here.
def callback(request):
    return None


def initiate_payment(request):
    return render(request, "payment.html")
