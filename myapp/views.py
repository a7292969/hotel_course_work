from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import CommentForm
from .models import Comment, Room


def index(req):
    return render(req, 'index.html')


def rooms(req):
    rooms = Room.objects.all()
    return render(req, 'rooms.html', {'rooms': rooms})


def room(req):
    room = Room.objects.get(id=req.GET['id'])
    return render(req, 'room.html', {'room': room})


def reviews(req):
    comments = Comment.objects.all()
    comment_form = CommentForm()
    return render(req, 'reviews.html', {'comments': comments, 'comment_form': comment_form})


def contacts(req):
    comment_form = CommentForm()
    return render(req, 'contacts.html', {'comment_form': comment_form})


def send_comment(req):
    form = CommentForm(req.POST)
    if not form.is_valid():
        return HttpResponse(status=400)
    user = Comment.objects.create(
        name=form.cleaned_data['name'], text=form.cleaned_data['text'])

    return redirect('/')
