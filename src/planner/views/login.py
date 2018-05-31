from django.views.generic import TemplateView

class LoginView(TemplateView):
    template_name = "planner/user_login_page.html"
