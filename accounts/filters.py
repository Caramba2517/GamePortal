from django_filters import FilterSet, CharFilter, DateFilter, ModelChoiceFilter, BooleanFilter
from ads.models import Ads, Reply, User


def req_reply(request):
    if request is None:
        return Reply.objects.none()
    reply = Ads.objects.filter(author=request.user).all()
    return reply


class ReplyFilter(FilterSet):
    ad = ModelChoiceFilter(queryset=req_reply)

    class Meta:
        model = Reply
        fields = {'ad': ['exact']}


