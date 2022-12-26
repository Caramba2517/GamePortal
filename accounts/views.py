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
    reply_filter = ReplyFilter(request.GET,
                               request=request,
                               queryset=Reply.objects.filter(ad__author=request.user)
                               )

    context = {
        'replies': reply_filter.qs,
        'form': reply_filter.form,


    }
    return render(request, 'profile.html', context)


