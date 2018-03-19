from django.contrib import admin
from ordem.models import produto_item, servico_item, ordens


admin.site.register(produto_item)
admin.site.register(servico_item)
admin.site.register(ordens)