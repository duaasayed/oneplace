from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
from .backend import get_scrapables

def index(request):
    return render(request, 'scrapping/index.html')


@require_http_methods(["POST"])
def search(request):
    query = request.POST['q']
    query = '-'.join(query.split(' '))
    results = []
    for scrapable in get_scrapables(query):
        results += scrapable.scrape()
    request.session['results'] = results
    return redirect(f'/results?query={query}')


def results(request):
    res = request.session['results']
    paginator = Paginator(res, 5)
    page_number = request.GET['page'] if 'page' in request.GET else 1
    page_obj = paginator.get_page(page_number)
    return render(request, 'scrapping/results.html', {'page_obj': page_obj})


