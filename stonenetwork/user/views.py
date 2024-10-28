from django.views.generic.detail import DetailView
from user.models import User

class UserDetailView(DetailView):
    model = User
    template_name = 'user/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context