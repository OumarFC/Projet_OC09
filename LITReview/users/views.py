from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    title = "S'enregistrer"
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Compte créé avec succès !')
            return redirect('login')

    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form,
                                                   'title': title
                                                   })
