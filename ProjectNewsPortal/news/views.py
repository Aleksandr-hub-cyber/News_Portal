from django.views.generic import ListView, DetailView
from .models import *
from datetime import datetime


class PostList(ListView):

    model = Post

    ordering = '-time_create'

    template_name = 'news.html'

    context_object_name = 'post'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['time_now'] = datetime.utcnow()

        context['next_sale'] = None
        return context


class PostDetail(DetailView):

    model = Post

    template_name = 'news_detail.html'

    context_object_name = 'post'


        context = super().get_context_data(**kwargs)
        context["time_now"] = datetime.utcnow()

        return context
