from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


class IndexView(TemplateView):

    template_name = "planner/planner_index.html"

    @method_decorator(login_required)
    def dispatch(self,*args, **kwargs):
        return super().dispatch(*args, **kwargs)
