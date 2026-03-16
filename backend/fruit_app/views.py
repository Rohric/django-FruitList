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
        {"name": "Apfel",
         "gewicht": 150,
         "farbe": "rot",
         "img": "fruit_app/img/apfel.jpg",
         "is_ordered": True},
        {"name": "Banane",
         "gewicht": 120,
         "farbe": "gelb",
         "img": "fruit_app/img/banane.jpg",
         "is_ordered": True},
        {"name": "Orange",
         "gewicht": 180,
         "farbe": "orange",
         "img": "fruit_app/img/orange.jpg",
         "is_ordered": False},
        {"name": "Kiwi",
         "gewicht": 90,
         "farbe": "braun",
         "img": "fruit_app/img/kiwi.jpg",
         "is_ordered": False},
        {"name": "Traube",
         "gewicht": 5,
         "farbe": "lila",
         "img": "fruit_app/img/traube.jpg",
         "is_ordered": True}
    ]
    return render(request, "fruit_app/fruitlist.html", {"fruits": fruits})


def info(request):
    return render(request, "fruit_app/info.html")
