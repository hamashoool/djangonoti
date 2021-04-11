from django.shortcuts import render, get_object_or_404

from major.models import Notification


def home(request):
    context = {}

    user_notis = Notification.objects.filter(user=request.user).order_by('-id')
    context['notifications'] = user_notis

    return render(request, 'major/index.html')


def noties(request):
    context = {}

    user_notis = Notification.objects.filter(user=request.user).order_by('-id')
    context['notifications'] = user_notis

    return render(request, 'major/noties.html', context)


def noti(request, pk):
    noti_ = get_object_or_404(Notification, id=pk)

    return render(request, 'major/noti.html', {"noti": noti_})