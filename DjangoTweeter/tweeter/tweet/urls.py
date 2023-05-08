from django.shortcuts import render
from . import views


##urlpatterns = [
## path('welcome/', views.welcome, name='home'),
def welcome(request):
    return render(request, "home.html")
##]
