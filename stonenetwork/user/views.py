from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from user.models import User

class UserDetailView(DetailView):
    model = User
    template_name = 'user/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserCreateView(CreateView):
    model = User
    template_name = 'user/user_create.html'
    fields = ['nick', 'first_name', 'last_name', 'email', 'avatar', 'identify']
    success_url = '/user/{id}'