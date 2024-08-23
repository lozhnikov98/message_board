from django.urls import path

from .views import *

urlpatterns = [
    path('', MsgView.as_view(), name='Messages'),
    path('create/', MsgCreate.as_view(), name='Create'),
    path('<int:pk>', MsgDetail.as_view(), name='Message'),
    path('<int:pk>/comments', comment, name='Comments'),
    path('comm/', MyCommentList.as_view(), name='comm'),
    path('<int:pk>/edit', MsgEdit.as_view(), name='edit'),
    path('<int:pk>/delete', MsgDel.as_view(), name='delete'),
    path('<int:pk>/addcomment', CommCreate.as_view(), name='addcomm'),
    path('profile', profile, name='profile'),
    path('comments/<int:pk>', OneComm.as_view(), name='onecomm'),
    path('comments/<int:pk>/delete', CommDel.as_view(), name='delcomm'),
    path('comments/<int:pk>/confirm', CommConfirm.as_view(), name='confirm'),
]
