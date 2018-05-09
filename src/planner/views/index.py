from django.views.generic import DetailView


class IndexView(DetailView):

    template_name = "planner/planner_index.html"
