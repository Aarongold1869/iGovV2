from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from .models import *

# Create your views here.
def home_page(request):
    return render(request,"igov/home.html")

def bill_list_view(request):
    qs = Bill.objects.all()
    template = 'legislation/bill_list_page.html'
    # template = 'legislation/legislation_blog_rss.html'    
    context = {'bill_list': qs}
    return render(request, template, context)

