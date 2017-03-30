from django.shortcuts import render, get_object_or_404, redirect, reverse
from museums.models import Museum
from forms import AddMuseumForm
from pieces.models import Piece
from pieces.forms import AddPieceForm

# Create your views here.

def my_museums(request):
    museums = Museum.objects.all()
    return render(request, "my_museums.html", {'museums':museums})

def museum_detail(request, id):
    museum = get_object_or_404(Museum, pk=id)
    pieces = Piece.objects.filter(museum=museum)
    args = {'museum':museum, 'pieces':pieces}
    return render(request, "museum_detail.html", args)

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

def add_piece_to_museum(request, id):
    museum = get_object_or_404(Museum, pk=id)
    if request.method == 'POST':
        form = AddPieceForm(request.POST, request.FILES)
        if form.is_valid():
            piece = form.save(commit=False)
            piece.museum=museum
            piece.save()
            return redirect(museum_detail, id)
    else:
        form = AddPieceForm()
    return render(request, 'add_piece.html', {'form':form})

def pieces_details(request, id):
    piece = get_object_or_404(Piece, pk=id)
    museum = piece.museum
    return render(request, 'piece_details.html', {'piece':piece, 'museum': museum})

def edit_piece(request, id):
    piece_edited = get_object_or_404(Piece, pk=id)
    if request.method == 'POST':
        form = AddPieceForm(request.POST, request.FILES, instance=piece_edited)
        if form.is_valid():
            piece_edited = form.save(commit=False)
            piece_edited.save()
            return redirect(pieces_details, piece_edited.pk)
    else:
        form = AddPieceForm(instance=piece_edited)
    args = {'form':form, 'piece_edited':piece_edited}
    return render(request, 'edit_piece.html', args )

def remove_piece(request, id):
    piece = Piece.objects.get(id=id)
    museum = piece.museum
    piece.delete()
    return redirect(museum_detail, museum.id)