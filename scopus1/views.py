from django.shortcuts import render
from .models import  *


def paper (request):
    obj3 = Paper.objects.all()
    obj1 = Authors.objects.all()
    obj2 = P_type.objects.all()
    papers = obj3.order_by('author_id')
    obj4 = request.GET.get('unread', False)
    return render(request, 'scopus1/index.html', context={'staff':obj1,'paper':papers,'ptype':obj2})