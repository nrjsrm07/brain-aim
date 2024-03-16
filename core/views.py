from django.shortcuts import render
from django.views import View

# Create your views here.
class Home(View):
    def get(self, request):
        error_message = request.GET.get('error_message', None)
        context = {'error_message': error_message}
        return render(request, 'core/home.html', context)
    
