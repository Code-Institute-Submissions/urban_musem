from django.shortcuts import render, get_object_or_404, redirect, reverse
from museums.models import Museum
from forms import AddMuseumForm

# Create your views here.

def my_museums(request):
    museums = Museum.objects.all()
    return render(request, "my_museums.html", {'museums':museums})

def museum_detail(request, id):
    museum = get_object_or_404(Museum, pk=id)
    return render(request, "museum_detail.html", {'museum':museum})

def add_museum(request):
    if request.method == 'POST':
        form = AddMuseumForm(request.POST)
        if form.is_valid():
            museum = form.save(commit=False)
            museum.save()
            return redirect(museum_detail, museum.pk)
    else:
        form = AddMuseumForm()
    return render(request, 'new_museum.html', {'form':form})

def edit_museum(request, id):
    museum_edited = get_object_or_404(Museum, pk=id)
    if request.method == 'POST':
        form = AddMuseumForm(request.POST, instance=museum_edited)
        if form.is_valid():
            museum_edited = form.save(commit=False)
            museum_edited.save()
            return redirect(museum_detail, museum_edited.pk)
    else:
        form = AddMuseumForm(instance=museum_edited)
    return render(request, 'edit_museum.html', {'form':form})

def remove_museum(request, id):
    Museum.objects.get(id=id).delete()
    return redirect(reverse('my_museums'))

