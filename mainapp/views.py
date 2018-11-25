from django.shortcuts import render

# Create your views here.
def main_view(request):
    return render(request, 'mainapp/index.html')

def projects_view(request):
    return render(request, 'mainapp/projects.html')

def contacts_view(request):
    return render(request, 'mainapp/contacts.html')