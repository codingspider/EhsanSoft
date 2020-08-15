from django.contrib import admin

# Register your models here.
from .models import *


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('title',)

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
admin.site.register(Subscriber)