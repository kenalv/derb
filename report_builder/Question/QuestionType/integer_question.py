'''
Created on 14/9/2016

@author: natalia
'''
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.utils import timezone

from report_builder.Question.QuestionView import QuestionViewAdmin, QuestionViewResp, QuestionViewPDF


class miContexto(object):

    def get_context_data(self, **kwargs):
        contex = ListView.get_context_data(self, **kwargs)
        contex['datetime'] = timezone.now()
        return contex

class IntegerQuestionAdmin(QuestionViewAdmin):
    def hola(self):
        return print("hola")


    