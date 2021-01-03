from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, Http404
from Card.base import *

class MainView(View):
    def get(self, request):
        return render(request, 'index.html', context={'tours': tours.items(),
                                                            'keysdep': departures.items(),
                                                            'departures': departures,
                                                            'random6' : random6,
                                                            })
class DepartureView(View):
    def get(self, request, departure,  *args, **kwargs):
        if departure not in departures:
            raise Http404
        return render(request, 'departure.html', context={'tours': tours.items(),
                                                                'from': departures[departure],
                                                                'departure': departure,
                                                                'departures': departures,
                                                                'keysdep' : departures.items(),
                                                                'tourcount' : tourcount[departure],
                                                                'pricemin' : pricemin[departure],
                                                                'pricemax' : pricemax[departure],
                                                                'nightsmin': nightsmin[departure],
                                                                'nightsmax': nightsmax[departure],
                                                                })


class TourView(View):
    def get(self, request, nomer, *args, **kwargs):
          if nomer not in range(1,17):
              raise Http404
          return render(request, 'tour.html', context={'tours': tours[nomer],
                                                             'departure': departures[tours[nomer]['departure']],
                                                             'keysdep' : departures.items(),
                                                             'departures': departures,

                                                             })