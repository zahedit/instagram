from django.urls import path, include
from relation.views import FollowUnfollowCreateDestroyView

urlpatterns = [
    path('<str:username>/follow/', FollowUnfollowCreateDestroyView.as_view(), name='follow-unfollow'),
]
