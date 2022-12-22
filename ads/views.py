from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView, UpdateView
from .models import Ads, Reply
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from ads.forms import AdsForm, ReplyForm

# Create your views here.

class AdsList(ListView):
    model = Ads
    ordering = 'time_create'
    template_name = 'ads.html'
    context_object_name = 'ads'
    paginate_by = 10


class AdsDetail(DetailView):
    model = Ads
    template_name = 'ad.html'
    context_object_name = 'ad'


@login_required
def create_reply(request, pk):
    form = ReplyForm()
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            new_reply = form.save(commit=False)
            new_reply.author = request.user
            new_reply.ad = Ads.objects.get(pk=pk)
            new_reply.save()
            return HttpResponseRedirect('/ads/')
    return render(request, 'reply.html', {'form': form})


@login_required
def create_ad(request):
    form = AdsForm()
    if request.method == 'POST':
        form = AdsForm(request.POST)
        if form.is_valid():
            new_ad = form.save(commit=False)
            new_ad.author = request.user
            new_ad.save()
            return HttpResponseRedirect('/ads/')
    return render(request, 'ads_edit.html', {'form': form})


class ReplayDetail(LoginRequiredMixin, DetailView):
    model = Reply
    context_object_name = 'reply'


class ReplyDelete(LoginRequiredMixin, DeleteView):
    model = Reply
    template_name = 'reply_delete.html'
    context_object_name = 'reply_delete'
    success_url = reverse_lazy('profile')

