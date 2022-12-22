from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from ads.models import User, Reply, Ads
from accounts.filters import ReplyFilter
from accounts.forms import ReplyForm


@login_required
def profile(request):
    reply_list = Reply.objects.filter(ad__author=request.user)
    reply_filter = ReplyFilter(request.GET,
                               queryset=Reply.objects.filter(ad__author=request.user)
                               )
    paginator = Paginator(reply_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'replies': reply_filter.qs,
        'form': reply_filter.form,
        'paje_obj': page_obj,

    }
    return render(request, 'profile.html', context)


