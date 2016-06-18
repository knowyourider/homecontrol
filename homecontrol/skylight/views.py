from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView

from .forms import ControlForm

from .yocto_skylight import *
#import yocto_skylight

def index(request):
    message = relay_control("VeluxControl", "2") # , "B"
    return HttpResponse("Hello, world. " + message)


def controlXX(request):
    """
    non class based view abandone
    """
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ControlForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            action = form.cleaned_data['action']
            message = relay_control("VeluxControl", action) # , "B"
            # redirect to a new URL:
            # return HttpResponseRedirect('/velux/control/')
            return HttpResponse("form submitted: " + message)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ControlForm()

    return render(request, 'control_form.html', {'form': form})


class ControlView(FormView):
    template_name = 'control_form.html'
    form_class = ControlForm
    initial = {'message': 'result message will appear here'}
    #success_url = '/thanks/'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            action = form.cleaned_data['action']
            message = relay_control("VeluxControl", action)

            return render(request, self.template_name, {'form': form, 'message': message})
        # this will return error if form is not valid
        return render(request, self.template_name, {'form': form})
