from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView

from .forms import CustomSignupForm
from .models import Authors


class SignUp(CreateView):
    model = User
    form_class = CustomSignupForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'


class ConfirmUser(UpdateView):
    models = Authors
    context_object_name = 'confirm_user'

    def post(self, request, *args, **kwargs):
        if 'code' in request.POST:
            otp = Authors.objects.filter(code=request.POST['code'])
            if otp.exists():
                user = Authors.objects.get(code=request.POST['code'])
                pk = user.authorUsers_id
                author = User.objects.get(id=pk)
                author.is_active = True
                author.save()
            else:
                return render(self.request, 'users/invalide_code.html')
            a = Authors.objects.get(code=request.POST['code'])
            a.delete()
        return redirect('account_login')
