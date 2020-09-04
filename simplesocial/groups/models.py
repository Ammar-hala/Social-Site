from django.db import models
from django.utils.text import slugify # converts string to lowercase... removes alphanum characters like space and puts _ underscore
# if u have string that has spaces in it and u want to use it as aprt of url slugify will arrange it
from django.urls import reverse
import misaka # can put down links or markdown text using it... pip install misaka
from django.contrib.auth import get_user_model #returns user model that is active in this project
User = get_user_model()

from django import template
register = template.Library() # this is how we can use custom template tags
# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=256 , unique=True) # unique cos dont want groups to have same names
    slug = models.SlugField(allow_unicode=True , unique=True) # unique so all url codes are diff for diff groups
    description = models.TextField(blank=True , default='') #  desc can be blank so black = true.. default value will be ''
    description_html = models.TextField(editable=False , default='' , blank=True) # is not editable.. can be blank
    members = models.ManyToManyField(User , through='GroupMember') # through GroupMember class

    def __str__(self):
        return self.name

    def save(self , *args , **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description) # in case we have markdown in desc we can call it by misaka
        super().save(*args , **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single' , kwargs={"slug" : self.slug} )

    class Meta():
        ordering = ['name']

class GroupMember(models.Model):
    group = models.ForeignKey(Group , related_name='memberships' , on_delete=models.CASCADE)
    user = models.ForeignKey(User , related_name='user_groups' , on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta():
        unique_together = ('group' , 'user') #will explain later


# Group Member class connects to the group and user which is activated
# Group Class name , description , slug , description_html that we will use with misaka to get some markdwon text...
# and finally we have which has ManyToManyField which means all the members which is connected to that Group
