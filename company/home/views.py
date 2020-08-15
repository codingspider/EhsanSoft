import os
import sys
sys.path.append(os.path.realpath('.'))
from ckeditor.widgets import LazyEncoder
from django.shortcuts import render, redirect
from  booksoft.models import *
from commerce.models import *
from loyalty.models import *
from crm.models import *
from onlinetraining.models import *
from customerfeedback.models import *
from fulstack.models import *
from school.models import *
from django.http import JsonResponse, HttpResponse
from marketing.models import *
from school.models import SchoolLogo
from django.core.serializers import serialize
from .models import *


def home(request):
    header = HeaderHome.objects.get()
    global_secure = GlobalSecure.objects.get()
    personalized_support = PersonalizedSupport.objects.get()
    quick_to_market = QuickToMarket.objects.get()
    advantage = Advantage.objects.get()
    open_to_integrate = OpenToIntegrations.objects.get()
    smart_connected = SmartConnected.objects.get()
    one_platform = OnePlatform.objects.get()
    everything_connects = EverythingConnects.objects.get()
    partner_with = PartnerWith.objects.get()
    retailer = Retailers.objects.get()
    distributors = Distributors.objects.get()
    manufactures = Manufacturers.objects.get()
    loyalty_and_incentive = LoyaltyAndIncentives.objects.get()
    b2b_commerce = B2BCommerce.objects.get()

    return render(request, 'home/home.html', {
        'header': header,
        'global_secure': global_secure,
        'personalized_support': personalized_support,
        'quick_to_market': quick_to_market,
        'advantage': advantage,
        'open_to_integrate': open_to_integrate,
        'smart_connected': smart_connected,
        'one_platform': one_platform,
        'everything_connects': everything_connects,
        'partner_with': partner_with,
        'retailer': retailer,
        'distributors': distributors,
        'manufactures': manufactures,
        'loyalty_and_incentive': loyalty_and_incentive,
        'b2b_commerce': b2b_commerce,
    })


def commerce(request):
    commerce = Commerce.objects.all()
    everything = EverythingYouNeed.objects.all()
    multipleway = MultipleWayOrder.objects.get()
    simpleorder = SimplifyingOrder.objects.get()
    commerce_header = CommerceHeader.objects.get()
    return render(request, 'home/commerce.html', {'commerce': commerce, 'everything': everything, 'multipleway':multipleway, 'simpleorder': simpleorder, 'header': commerce_header})


def loyalty(request):
    loyalty_header = LoyaltyHeader.objects.get()
    intencent = IntentBuying.objects.all()
    trade_loyalty = TradeLoyalty.objects.all()
    modular_meet = ModularLoyalty.objects.get()
    leader_loyalty = LeaderboardLoyalty.objects.all()
    return render(request, 'home/loyality.html', {'header': loyalty_header, 'intencent': intencent, 'trade_loyalty': trade_loyalty, 'modular_meet': modular_meet, 'leader_loyalty': leader_loyalty})


def marketing(request):
    marketing_header = MarketingHeader.objects.get()
    div_one = DivOne.objects.get()
    div_two = DivTwo.objects.get()
    div_3_marketing = DivThree.objects.get()
    marketing_tools = MarketingTool.objects.all()
    return render(request, 'home/marketing.html', {'header': marketing_header, 'div_one': div_one, 'div_two': div_two, 'div_three': div_3_marketing, 'marketing_tools': marketing_tools})





def crm(request):
    header = CrmHeader.objects.get()
    div_one = CrmDivOne.objects.all()
    return render(request, 'home/crm.html', {
        'header': header,
        'div_one': div_one
    })


def online(request):
    header = OnlineTrainginHeader.objects.get()
    div_one = DivOne.objects.get()
    div_two =DivTwo.objects.get()
    div_three=DivThree.objects.get
    div_four=DivFour.objects.get()

    return render(request, 'home/online.html', {
        'header': header,
        'div_one': div_one,
        'div_two': div_two,
        'div_three': div_three,
        'div_four': div_four
    })


def feedback(request):
    header = CustomerFeedbackHeader.objects.get()
    div_one = DivOne.objects.get()
    div_two = DivTwo.objects.get()
    div_three = DivThree.objects.get()
    return render(request, 'home/feedback.html', {
        'div_one': div_one,
        'div_two': div_two,
        'div_three': div_three,
        'header': header

    })


def bookasoft(request):
    description = BookSoftDescription.objects.get()
    bookasoft_header = BookSoftHeader.objects.get()
    return render(request, 'home/bookasoft.html', {'description': description, 'header': bookasoft_header})


def contact(request):
    return render(request, 'home/contact.html')


def partners(request):
    header = 'Ehsan Software creates strategic partnerships with companies around the world to deliver outstanding results for brands.'
    return render(request, 'home/partners.html', {'header': header})


def admincrm(request):
    header = FullStackHeader.objects.get()
    div1data = DivOne.objects.get()
    div2data = DivTwo.objects.get()
    div3data = DivThree.objects.all()
    div4data = DivFour.objects.get()
    div5data = DivFive.objects.all()
    div6data = DivSix.objects.all()
    return render(request, 'home/admincrm.html', {
        'header': header,
        'div1': div1data,
        'div2': div2data,
        'div3': div3data,
        'div4': div4data,
        'div5': div5data,
        'div6': div6data
    })


def likePost(request):
    if request.method == 'GET':
        bar = serialize('json', SchoolLogo.objects.all(), cls=LazyEncoder)
        return JsonResponse(bar, safe=False)
    else:
        return HttpResponse("Request method is not a GET")


def school_details(self, request, *args, **kwargs):
    pass


def subscriber(request):
    if request.method == 'POST':
        if request.POST.get('subscriber'):
            post = Subscriber()
            post.title = request.POST.get('subscriber')
            post.save()
    return redirect('/')


