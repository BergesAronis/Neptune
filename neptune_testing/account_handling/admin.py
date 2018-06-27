from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Agent, Client, User
#
# class AgentInline(admin.StackedInline):
#     model = Agent
#     can_delete = False
#
#
# class ClientInline(admin.StackedInline):
#     model = Client
#     can_delete = False
#
#
# class CustomUserAdmin(UserAdmin):
#     inlines = (AgentInline, ClientInline, )
#
#     def get_inline_instances(self, request, obj=None):
#         if not obj:
#             return list()
#         return super(CustomUserAdmin, self).get_inline_instances(request, obj)
#
# Register your models here.
# admin.site.unregister(User)
admin.site.register(User)
