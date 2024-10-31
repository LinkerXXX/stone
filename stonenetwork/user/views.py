from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from user.models import User
from user.forms import MOD_UserCreateForm, UserAuthForm
from django.urls import reverse_lazy


class UserDetailView(DetailView):
    model = User
    template_name = 'user/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserCreateView(CreateView):
    model = User
    template_name = 'user/user_create.html'
    form_class = MOD_UserCreateForm
    success_url = '/user/{id}'


class UserLoginView(LoginView):
    form_class = UserAuthForm
    template_name = 'user/user_login.html'

    def get_success_url(self):
        user_id = self.request.user.id
        return reverse_lazy('user_detail', kwargs={'pk': user_id})
