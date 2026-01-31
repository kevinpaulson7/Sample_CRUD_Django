from django.shortcuts import render, redirect, get_object_or_404
from .models import Bike
from .forms import BikeForm

# READ
def bike_list(request):
    bikes = Bike.objects.all()
    return render(request, 'bike_list.html', {'bikes': bikes})

# CREATE
def bike_create(request):
    form = BikeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('bike_list')
    return render(request, 'bike_form.html', {'form': form})

# UPDATE
def bike_update(request, id):
    bike = get_object_or_404(Bike, id=id)
    form = BikeForm(request.POST, instance=bike)
    if form.is_valid():
        form.save()
        return redirect('bike_list')
    return render(request, 'bike_form.html', {'form': form})

# DELETE
def bike_delete(request, id):
    bike = get_object_or_404(Bike, id=id)
    if request.method == 'POST':
        bike.delete()
        return redirect('bike_list')
    return render(request, 'bike_confirm_delete.html', {'bike': bike})
