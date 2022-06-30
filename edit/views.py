from django.shortcuts import render, redirect
from account.forms import RegistrationForm
from account.models import Account


def profile(request):
    profile = Account.objects.all()
    email = profile.email
    if request.method != 'POST':
        form = RegistrationForm(instance=profile)
    else:
        form = RegistrationForm(instance=profile, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:profile', email_id=email.id)
    context = {'form': form, 'email': email}
    return render(request, 'edit/profile.html', context)