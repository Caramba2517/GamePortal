from django_filters import ChoiceFilter, FilterSet, CharFilter, DateFilter, ModelChoiceFilter, BooleanFilter
from ads.models import Ads, Reply, User, Category


def req_reply(request):
    if request is None:
        return Reply.objects.none()
    reply = Ads.objects.filter(author=request.user).all()
    return reply


class ReplyFilter(FilterSet):
    ad = ChoiceFilter()

    class Meta:
        model = Reply
        fields = ['ad']

    def __init__(self, *args, **kwargs):
        super(ReplyFilter, self).__init__(*args, **kwargs)
        self.filters['ad'].extra.update(
            {
                'choices': kwargs['request']
            }
        )

