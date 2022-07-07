from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#from adrs_lm.leave_manager.models import LeaveType
from leave_manager.models import Leave

# Create your views here.


class LeaveList(ListView):
    model = Leave
    context_object_name = 'leaves'


class LeaveDetail(DetailView):
    model = Leave
    context_object_name = "leave"
    template_name = 'leave_manager/leave_detail.html'


class LeaveCreate(CreateView):
    model = Leave
    fields = '__all__'
    success_url = reverse_lazy('leaves')


class LeaveUpdate(UpdateView):
    model = Leave
    fields = '__all__'
    success_url = reverse_lazy('leaves')


class DeleteView(DeleteView):
    model = Leave
    context_object_name = 'leaves'
    success_url = reverse_lazy('leaves')
