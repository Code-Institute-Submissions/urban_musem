from django.shortcuts import render, get_object_or_404,redirect, reverse
from pieces.models import Piece
from pieces.forms import AddPieceForm

# Create your views here.

def pieces_list(request):
    pieces = Piece.objects.all()
    return render(request, 'pieces_list.html', {'pieces':pieces})

def pieces_details(request, id):
    piece = get_object_or_404(Piece, pk=id)
    return render(request, 'piece_details.html', {'piece':piece})

def add_piece(request):
    if request.method == 'POST':
        form = AddPieceForm(request.POST, request.FILES)
        if form.is_valid():
            piece = form.save(commit=False)
            piece.save()
            return redirect(pieces_details, piece.pk)
    else:
        form = AddPieceForm()
    return render(request, 'add_piece.html', {'form':form})

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
    return render(request, 'edit_piece.html', {'form':form})

def remove_piece(request, id):
    Piece.objects.get(id=id).delete()
    return redirect(reverse('pieces_list'))