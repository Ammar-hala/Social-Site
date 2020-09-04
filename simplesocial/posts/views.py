from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (TemplateView , ListView , DetailView , CreateView , UpdateView , DeleteView)
from django.http import Http404

from django.contrib import messages

from braces.views import SelectRelatedMixin

from posts.models import Post
from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()

class PostList(ListView , SelectRelatedMixin):
    model = Post
    select_related = ('user' , 'group') # from Post model

class UserPosts(ListView):
    model = Post
    template_name = 'posts/user_post_list.html'

    #have to add some methods to make sure this works correctly  when logged in user

    def get_queryset(self): # check if username is qual to get username of who is logged in rn
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact = self.kwargs.get('username')) # check in doc
            # if goto user posts..for post's user.. grab all posts related to that exact tusername
        except User.DoesNotExist:
            raise Http404

        else:
            return self.post_user.posts.all()


    def get_context_data(self , **kwargs): # grabs post_user and return context dictionary off of that
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context


# Detail View
class PostDetail(DetailView , SelectRelatedMixin):
    model = Post
    select_related = ('user' , 'group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact = self.kwargs.get('username'))


#Create Post

class CreatePost(LoginRequiredMixin , CreateView , SelectRelatedMixin):
    fields = ('message' , 'group')
    model = Post

    def form_valid(self , form): # cehcking form is valid.. acnd connecting post to the user
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save() # to connect actual post to user itself
        return super().form_valid(form)

            # A lot of thing s/ variable comes with generic classes we're not amking them
#Delete Post
class DeletePost(SelectRelatedMixin , LoginRequiredMixin , DeleteView):
    model = Post
    select_related = ('user' , 'group')
    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self , *args , **kwargs): # return message that post was deleted
        messages.success(self.request , 'Post Deleted')
        return super().delete(*args , **kwargs)
