from django.shortcuts import render,get_object_or_404
from workers.models import *
from django.db.models import Q
from django.views.generic import ListView,DetailView
class HomeView(ListView):
    queryset = Units.objects.all()[1:]
    context_object_name = 'units'
    template_name = 'home/index.html'
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['departaments']=Departaments.objects.all()
        context['unit']=Units.objects.first()
        return context
class UnitsDetailView(DetailView):
    model = Units
    context_object_name = 'unit'
    template_name = 'home/units_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['units'] = Units.objects.all().order_by('-id')
        return context

def departament_detail(request,slug):
    units=Units.objects.all().order_by('id')
    departament=get_object_or_404(Departaments,slug=slug)
    workers=Workers.objects.filter(deps=departament)
    a=[]
    b=[]
    for i,j in Workers.choices_status:
        a.append(i)
        b.append(j)
    return render(request,'home/departament_detail.html',locals())

def status_workers(request,slug,work):
    departament = get_object_or_404(Departaments, slug=slug)
    workers=Workers.objects.filter(status=work,deps=departament)
    a = []
    b = []
    for i, j in Workers.choices_status:
        a.append(i)
        b.append(j)
    return render(request, 'home/departament_detail.html', locals())
def worker_detail(request,slug):
    units = Units.objects.all()
    worker=get_object_or_404(Workers,slug=slug)
    return render(request,'home/worker_detail.html',locals())
def founded(request):
    units=Units.objects.all()
    query = request.GET.get('q')
    query=query.title()
    print(query)
    workers = Workers.objects.filter(
       Q(fullname__icontains=query) | Q(
            city__name__icontains=query) | Q(position__name__icontains=query)
        | Q(ip_number__icontains=query) | Q(mobile_phone__icontains=query) | Q(
            deps__departament_block__name__icontains=query) | Q(deps__name__icontains=query)
        | Q(deps__units__name__icontains=query)|Q(phone__icontains=query)
    )
    return render(request,'home/founded.html',locals())