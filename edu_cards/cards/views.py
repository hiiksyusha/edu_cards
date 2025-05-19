from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Card
from .forms import CardForm, CSVUploadForm
import csv
import io

def index(request):
    return render(request, 'cards/index.html')

def card_list(request):
    cards = Card.objects.all()
    return render(request, 'cards/table.html', {'cards': cards})

def card_view(request):
    cards = Card.objects.all()
    return render(request, 'cards/cards.html', {'cards': cards})

def add_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('card_list')
    else:
        form = CardForm()
    return render(request, 'cards/add_card.html', {'form': form})

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)  # skip header
            for row in csv.reader(io_string, delimiter=','):
                Card.objects.create(word=row[0], translation=row[1])
            return redirect('card_list')
    else:
        form = CSVUploadForm()
    return render(request, 'cards/upload.html', {'form': form})

def delete_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == 'POST':
        card.delete()
        return redirect('card_list')
    return render(request, 'cards/confirm_delete.html', {'card': card})

def edit_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES, instance=card)
        if form.is_valid():
            form.save()
            return redirect('card_list')
    else:
        form = CardForm(instance=card)
    return render(request, 'cards/edit_card.html', {'form': form, 'card': card})