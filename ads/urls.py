from django.urls import path
from .views import AdsList, AdsDetail, create_ad, create_reply, ReplyDelete, Aprove


urlpatterns = [
    path('', AdsList.as_view(), name='ads'),
    path('<int:pk>', AdsDetail.as_view(), name='ad'),
    path('<int:pk>/reply/', create_reply, name='create_reply'),
    path('reply/<int:pk>/delete/', ReplyDelete.as_view(), name='replay_delete'),
    path('create/', create_ad, name='create_ad'),
    path('reply/<int:pk>/aprove/', Aprove.as_view(), name='aprove'),

]