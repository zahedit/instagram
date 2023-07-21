from django.views import View
from django.http import Http404
from django.contrib.auth import login, get_user_model
from relation.models import Relation
from django.shortcuts import redirect
from django.urls import reverse


User = get_user_model()

class FollowUnfollowCreateDestroyView(View):

    def get_object(self):
        try:
            user = User.objects.get(username= self.kwargs.get('username')) #find the user that, the user asked
        except User.DoesNotExist: # if the user doesn't exist
            raise Http404
        return user
    
    def post(self, request, username, *args, **kwargs):
        target_user = self.get_object()
        qs = Relation.objects.filter(from_user= request.user, to_user= target_user)
        if request.user == target_user:
            return redirect(reverse('profile', args=[target_user.username]))
        
        if qs.exists():
            qs.delete()
        else:
            Relation.objects.create(from_user= request.user, to_user= target_user)

        # return redirect('/{}/'.format(target_user.username))
        return redirect(reverse('profile', args=[target_user.username]))