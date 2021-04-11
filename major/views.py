from django.shortcuts import render


# home function view
def home(request):
    return render(request, 'major/index.html')
