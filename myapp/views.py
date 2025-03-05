from django.shortcuts import render , redirect
from .forms import MessageForm
from .models import Message
# Create your views here.

def profile(request):
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = MessageForm()
        
    return render(request, 'myapp/profile.html', {'form': form})

def inbox_view(request):
    messages = Message.objects.all()
    return render(request, 'myapp/inbox.html', {'messages': messages})

def message_delete(request, message_id):
    message = Message.objects.get(id=message_id)
    message.delete()
    return redirect('inbox')

def message_reply(request, message_id):
    message = Message.objects.get(id=message_id)
    return redirect('inbox')

