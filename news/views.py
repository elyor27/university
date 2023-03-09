from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from news.forms import NewsModelForm, CategoryModel
from django.urls import reverse


class NewsListViews(ListView):
    template_name = 'index.html'
    paginate_by = 6

    def get_queryset(self):
        qs = NewsModel.objects.order_by('-pk')
        q = self.request.GET.get('q')

        cat = self.request.GET.get('cat')

        if q:
            qs = qs.filter(title__icontains=q)
        if cat:
            qs = qs.filter(category__id=cat)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        return context


class NewsCreateViews(CreateView):
    form_class = NewsModelForm
    template_name = 'form.html'

    def get_success_url(self):
        return reverse('news:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        return context


class NewsUpdateView(UpdateView):
    form_class = NewsModelForm
    template_name = 'form.html'
    model = NewsModel

    def get_success_url(self):
        return reverse('news:list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        return context


class NewsDeleteViews(DeleteView):
    model = NewsModel

    def get_success_url(self):
        return reverse('news:list')


class NewsDateilViews(DetailView):
    model = NewsModel
    template_name = 'News_detail.html'
