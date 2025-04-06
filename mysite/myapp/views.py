from django.shortcuts import render, redirect
from .models import Food, Consume
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# View to display the index page, where food items can be tracked
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

        # Save consumed food for the authenticated user
        consumed_entry = Consume(user=request.user, food_consumed=food_item)
        consumed_entry.save()

    foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)

    return render(request, 'myapp/index.html', {'foods': foods, 'consumed_food': consumed_food})

# View to delete consumed food
@login_required
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

# View to handle user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect('/')  # Redirect to the home page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
