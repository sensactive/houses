from django.shortcuts import render

# Create your views here.
def main_view(request):
    typesItem = [
        {'name': 'aspen', 'src': 'images/types/aspen.jpg'},
        {'name': 'heaven', 'src': 'images/types/heaven.jpg'},
        {'name': 'veil', 'src': 'images/types/veil.jpg'},
        {'name': 'tower', 'src': 'images/types/tower.jpg'},

    ]
    return render(request, 'mainapp/index.html',  {'typeItems': typesItem})

def projects_view(request):
    typesItem = [
        {'name': 'aspen', 'src': 'images/types/aspen.jpg', 'price': '300000'},
        {'name': 'heaven', 'src': 'images/types/heaven.jpg', 'price': '350000'},
        {'name': 'veil', 'src': 'images/types/veil.jpg', 'price': '400000'},
        {'name': 'tower', 'src': 'images/types/tower.jpg', 'price': '450000'},

    ]
    return render(request, 'mainapp/projects.html', {'items': typesItem})

def contacts_view(request):
    return render(request, 'mainapp/contacts.html')