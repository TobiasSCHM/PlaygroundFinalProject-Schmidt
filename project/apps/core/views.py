from django.shortcuts import render

#renderiza el archivo al momento de solicitarse la urls
def index(request):
    
    return render(request, 'index.html', context={})
