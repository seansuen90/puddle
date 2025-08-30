from django.shortcuts import get_object_or_404, redirect, render

from .forms import ConversationMessageForm
from .models import Conversation
from item.models import Item

def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    if item.created_by == request.user:
        return redirect('dashboard:index')
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])
    if conversations:
        pass #redirect to conversation
    form = ConversationMessageForm()
    return render(request, 'conversation/new.html', {
        'form': form
    })