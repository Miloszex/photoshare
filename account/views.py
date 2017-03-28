from django.shortcuts import render
from .forms import UserRegistrationForm


def register(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            return render(request,'account/register_success.html', {'message': 'Success!'})

    else:
        form = UserRegistrationForm()

    return render(request, 'account/register.html', {'form': form})

