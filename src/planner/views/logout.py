from django.views.generic import TemplateView
from django.contrib.auth import logout as auth_logout
from django.views.generic import RedirectView

class LogoutView(RedirectView):
    url = "planner/user_login_page.html"

    def get(self,request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView,self).get(request, *args, **kwargs)
