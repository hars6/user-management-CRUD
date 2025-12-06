import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User

@csrf_exempt
def create_user(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        user = User.objects.create(
            name=data["name"],
            email=data["email"],
            age=data["age"]
        )
        return JsonResponse({"message": "User created", "id": user.id})

@csrf_exempt
def get_users(request):
    if request.method == "GET":
        users = list(User.objects.values())
        return JsonResponse(users, safe=False)

@csrf_exempt
def get_user(request, id):
    try:
        user = User.objects.get(id=id)
        return JsonResponse({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "age": user.age
        })
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)

@csrf_exempt
def update_user(request, id):
    if request.method == "PUT":
        try:
            user = User.objects.get(id=id)
            data = json.loads(request.body.decode("utf-8"))

            user.name = data["name"]
            user.email = data["email"]
            user.age = data["age"]
            user.save()

            return JsonResponse({"message": "User updated"})
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)

@csrf_exempt
def delete_user(request, id):
    if request.method == "DELETE":
        try:
            user = User.objects.get(id=id)
            user.delete()
            return JsonResponse({"message": "User deleted"})
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)
