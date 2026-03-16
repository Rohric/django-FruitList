from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse


# def send_fruits(request):
#     fruits = [
#         {"name": "Apfel", "gewicht": 150, "farbe": "rot"},
#         {"name": "Banane", "gewicht": 120, "farbe": "gelb"},
#         {"name": "Orange", "gewicht": 180, "farbe": "orange"},
#         {"name": "Kiwi", "gewicht": 90, "farbe": "braun"},
#         {"name": "Traube", "gewicht": 5, "farbe": "lila"}
#     ]
#     return JsonResponse(fruits, safe=False)


def send_fruits(request):
    fruits = [
        {"name": "Apfel", "gewicht": 150, "farbe": "rot"},
        {"name": "Banane", "gewicht": 120, "farbe": "gelb"},
        {"name": "Orange", "gewicht": 180, "farbe": "orange"},
        {"name": "Kiwi", "gewicht": 90, "farbe": "braun"},
        {"name": "Traube", "gewicht": 5, "farbe": "lila"}
    ]
    return render(request, "fruit_app/fruitlist.html", {"fruits": fruits})
