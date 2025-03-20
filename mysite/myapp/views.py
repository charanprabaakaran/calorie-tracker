from django.shortcuts import render, redirect
from .models import Food, Consume
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def index(request):
    if request.method == "POST":
        food_consumed_name = request.POST.get('food_consumed')
        
        # Check if the food item exists
        try:
            food_item = Food.objects.get(name=food_consumed_name)
        except Food.DoesNotExist:
            messages.error(request, "Food item not found.")
            return redirect('/')

        # Ensure the user is authenticated
        if request.user.is_authenticated:
            consumed_entry = Consume(user=request.user, food_consumed=food_item)
            consumed_entry.save()
        else:
            messages.error(request, "You must be logged in to track food.")
            return redirect('login')

    foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)

    return render(request, 'myapp/index.html', {'foods': foods, 'consumed_food': consumed_food})

def delete_consume(request, id):
    try:
        consumed_food = Consume.objects.get(id=id, user=request.user)
        if request.method == 'POST':
            consumed_food.delete()
            return redirect('/')
    except Consume.DoesNotExist:
        messages.error(request, "Invalid request.")
        return redirect('/')

    return render(request, 'myapp/delete.html')