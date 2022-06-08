from django.shortcuts import get_object_or_404, render
from .models import Category,Portfolio

def portfolio(request,category_slug=None):
    categories = None
    programs = None

    if category_slug!=None:
        categories = get_object_or_404(Category,slug = category_slug)
        programs = Portfolio.objects.filter(category = categories)
    else:
        programs = Portfolio.objects.all()
    links = Category.objects.all()
    return render(request, "resumeapp/portfolio.html", {
        'programs':programs,
        'links': links,
    })

def portfolio_detail(request,category_slug,program_slug):
    single_portfolio = Portfolio.objects.get(category__slug = category_slug , slug = program_slug)

    return render(request, 'resumeapp/single-portfolio.html', {
        "single_portfolio": single_portfolio
    })