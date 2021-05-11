from django.shortcuts import (
    render,
    HttpResponse,
    redirect,
)

from django.views.generic import (
    View,
    ListView,
    DetailView,
    FormView,
)

from django.urls import reverse_lazy

from deposits.models import Deposit
from deposits.forms import DepositForm


class AddDepositView(FormView):

    form_class = DepositForm
    template_name = 'form.html'
    success_url = reverse_lazy('deposit-list')

    def form_valid(self, form):

        #
        form.save()
        #
        response = super().form_valid(form)

        return response

        print(type(a))
class DepositListView(ListView):

    model = Deposit
    template_name = 'index.html'
