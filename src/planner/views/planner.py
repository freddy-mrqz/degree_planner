from django import views

from django.views.generic import DetailView

from planner.models import Planner


class PlannerDetail(DetailView):

    model = Planner

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the courses
        context['planner_*'] = Planner.objects.all()
        return context
