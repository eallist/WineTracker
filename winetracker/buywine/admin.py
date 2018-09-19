from django.contrib import admin
from .models import (Wine, WineComment, Varietal, Winery, WineryComment, Vineyard, VineyardComment, Vintner,
                     VintnerComment, WineryVintner, WineryAddress, Province, Country, State, Region, WineServed,
                     VineyardLocation)

admin.site.register(Wine)
admin.site.register(WineComment)
admin.site.register(Varietal)
admin.site.register(Winery)
admin.site.register(WineryComment)
admin.site.register(Vineyard)
admin.site.register(VineyardComment)
admin.site.register(Vintner)
admin.site.register(VintnerComment)
admin.site.register(WineryVintner)
admin.site.register(WineryAddress)
admin.site.register(VineyardLocation)
admin.site.register(Province)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(Region)
admin.site.register(WineServed)
