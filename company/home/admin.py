from django.contrib import admin

# Register your models here.
from .models import B2BCommerce
from .models import LoyaltyAndIncentives
from .models import Manufacturers
from .models import Distributors
from .models import Retailers
from .models import PartnerWith
from .models import EverythingConnects
from .models import OnePlatform
from .models import SmartConnected
from .models import OpenToIntegrations
from .models import GlobalSecure
from .models import Advantage
from .models import PersonalizedSupport
from .models import HeaderHome
from .models import QuickToMarket

admin.site.register(B2BCommerce)
admin.site.register(LoyaltyAndIncentives)
admin.site.register(Manufacturers)
admin.site.register(Distributors)
admin.site.register(Retailers)
admin.site.register(PartnerWith)
admin.site.register(EverythingConnects)
admin.site.register(SmartConnected)
admin.site.register(OpenToIntegrations)
admin.site.register(OnePlatform)
admin.site.register(GlobalSecure)
admin.site.register(Advantage)
admin.site.register(PersonalizedSupport)
admin.site.register(HeaderHome)
admin.site.register(QuickToMarket)