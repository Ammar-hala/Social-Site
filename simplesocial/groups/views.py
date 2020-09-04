from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin # checks that current user has all permission
from django.urls import reverse
from django.views.generic import (TemplateView , ListView , DetailView , CreateView , UpdateView , DeleteView
                                    , RedirectView)
from django.contrib import messages

from django.shortcuts import get_object_or_404
from groups.models import Group , GroupMember
from . import models
# Create your views here.

class CreateGroup(CreateView , LoginRequiredMixin):
    fields = ('name' , 'description')
    model = Group


class SingleGroup(DetailView):
    model = Group

class ListGroups(ListView):
    model = Group


# JOIN AND LEAVE GROUPS
# DESCRIPTIOM FOR BOTH GROUPS IS IN TEXT FILE IN FOLDER OF VIDEOS... DIDNT FIND ANY DIFF IN BOTH YET BUT HTAT CODE NOT WORKS

class JoinGroup(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get("slug"))

        try:
            GroupMember.objects.create(user=self.request.user,group=group)

        except IntegrityError:
            messages.warning(self.request,("Warning, already a member of {}".format(group.name)))

        else:
            messages.success(self.request,"You are now a member of the {} group.".format(group.name))

        return super().get(request, *args, **kwargs)


class LeaveGroup(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):

        try:

            membership = models.GroupMember.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get("slug")
            ).get()

        except models.GroupMember.DoesNotExist:
            messages.warning(
                self.request,
                "You can't leave this group because you aren't in it."
            )
        else:
            membership.delete()
            messages.success(
                self.request,
                "You have successfully left this group."
            )
        return super().get(request, *args, **kwargs)
