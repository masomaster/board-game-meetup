from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('games/', views.games_index, name='games_index'),
    path('games/<int:game_id>/', views.games_detail, name='games_detail'),
    path('games/create/', views.GameCreate.as_view(), name='games_create'),
    path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),
    path('meetings/', views.meetings_list, name='meetings_index'),
    path('meetings/<int:game_id>/create/', views.create_meeting, name='create_meeting'),
    path('meetings/<int:pk>/', views.MeetingDetail.as_view(), name='meetings_detail'),
    path('meetings/<int:pk>/update/', views.MeetingUpdate.as_view(), name='meeting_update'),
    path('meetings/<int:pk>/delete/', views.MeetingDelete.as_view(), name='meeting_delete'),
    path('meetings/<int:meeting_id>/join_meeting', views.join_meeting, name="join_meeting"),
    path('meetings/<int:meeting_id>/leave_meeting', views.leave_meeting, name="leave_meeting"),
]
