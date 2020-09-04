from django.contrib import admin
from groups.models import Group , GroupMember
# Register your models here.

class GroupMemberInline(admin.TabularInline):
    model = GroupMember # so can edit it inside from Group... since Group is it's parent

admin.site.register(Group)
