from BanalCast.models import Post
from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    postes = Post.objects.all().reverse()
    quantidade_poste = len(postes)

    paginator = Paginator(postes, 5)
    page_number = request.GET.get('page', 1)
    pages = paginator.page(page_number)

    return render(request, 'index.html', {
        'postes': pages,
        'qtd_poste': quantidade_poste,
    })

def post(request, poste_id):
    postes = Post.objects.get(pk=poste_id)
    return render(request, 'post.html', {
        'postes': postes
    })

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
