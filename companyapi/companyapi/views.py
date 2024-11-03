from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("Home page started")
    friends=[
        "sanket",
        "Jaddu",
        "ankita"
    ]
    return JsonResponse(friends,safe=False)