# -*- coding: utf-8 -*-

from django.views import generic

from form import MyModelForm
from models import MyModelFile_Widget


class Home(generic.ListView):
    model = MyModelFile_Widget
    template_name = "files_widget/home.html"

    def get_context_data(self, **kwargs):
        MyModel_list = MyModelFile_Widget.objects.all()
        kwargs['MyModel_list'] = MyModel_list
        context = super(Home, self).get_context_data(**kwargs)
        return context


class Create(generic.CreateView):
    model = MyModelFile_Widget
    form_class = MyModelForm
    success_url = '/'
    template_name = "files_widget/create.html"

    # def get_form(self, data=None, files=None, **kwargs):
    #     user = self.request.user
    #     return MyModelForm(data, file s, seller=user, **kwargs)