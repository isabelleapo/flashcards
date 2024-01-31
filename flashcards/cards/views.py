from django.shortcuts import render, redirect
from .models import FlashCard
from .forms import CreateCard
import random
from django.contrib.auth.decorators import login_required
from django.views import generic


@login_required(login_url="/login/")
def create_card(request):
    if request.method == 'POST':
        form = CreateCard(request.POST)
        if form.is_valid():
            # Retrieve cleaned data from the form
            side_A = form.cleaned_data['side_a']
            side_B = form.cleaned_data['side_b']

            # Create an instance of the model and save it
            FlashCard.objects.create(side_a=side_A, side_b=side_B)
            return redirect('create_card')
    else:
        form = CreateCard()

    return render(request, 'cards/create_card.html', {'form':form})

# @login_required
class FlashCardList(generic.ListView):
    model = FlashCard

class FlashCardDetail(generic.DetailView):
    model = FlashCard
    def get_object(self, queryset=None):
        return random.choice(FlashCard.objects.all())

