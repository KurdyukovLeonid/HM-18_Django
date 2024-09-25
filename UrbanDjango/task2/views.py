from django.shortcuts import render
from django.views import View

# Create your views here.
def func_template(request):
    return render(request, 'second_task/func_template.html')

# Классовое представление
class ClassTemplate(View):
    template_name = 'second_task/class_template.html'
    def get(self, request):
        return render(request, self.template_name)