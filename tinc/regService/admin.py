from django.contrib import admin

# Register your models here.

from .models import Node
from .models import Network

class NodeAdmin(admin.ModelAdmin):
  list_display = ('hostname', 'network', 'public_IP', 'config_IP', 'private_IP', )
  search_fields = ['hostname', 'network', 'public_IP', 'config_IP', 'private_IP']

admin.site.register(Node, NodeAdmin)


admin.site.register(Network)
