from django.shortcuts import render
from django.views.generic import View, DetailView, ListView


class IndexView(View):
    def get(self, request):
        return render(request, 'home.html')


home = IndexView.as_view()
