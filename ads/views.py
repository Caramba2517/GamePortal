from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView, UpdateView
from django.views.generic.edit import ModelFormMixin

from .models import Ads, Reply
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from ads.forms import AdsForm, ReplyForm, AproveForm


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


class Aprove(LoginRequiredMixin, ModelFormMixin, DetailView):
    model = Reply
    context_object_name = 'aprove'
    form_class = AproveForm
    template_name = 'aprove.html'

    def get_context_data(self, **kwargs):
        context = super(Aprove, self).get_context_data(**kwargs)
        context['form'] = self.get_form()

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
        else:
            return self.form_invalid(form)




class ReplyDelete(LoginRequiredMixin, DeleteView):
    model = Reply
    template_name = 'reply_delete.html'
    context_object_name = 'reply_delete'
    success_url = reverse_lazy('profile')
