import random
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.core.mail import send_mail

from .models import Authors


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.is_active = False
        Authors.objects.create(code=random.randint(100000, 999999), authorUsers=user)
        otp = Authors.objects.get(authorUsers=user)
        group = Group.objects.get(name="Authors")
        user.groups.add(group)
        user.save()
        send_mail(
            subject=f'Код активации',
            message=f'Код активации аккаунта: {otp.code}',
            from_email=None,
            recipient_list=[user.email],
        )
        return user
