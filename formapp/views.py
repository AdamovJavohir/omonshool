from django.shortcuts import render, redirect
from .form import RuyxatForm


# Create your views here.
def HomeView(request):
    if request.method == "POST":
        #form jo'natilgandan keyin obyekt yaratiladi
        form = RuyxatForm(request.POST)
        #form obyekti valid bo'lgani tekshiriladi
        if form.is_valid():
            #ma'lumot modelda saqlanadi
            form.save()
            #success nomli urlga yo'naltiradi
            return redirect('success')
    else:
        form = RuyxatForm()
    
    return render(request, 'home.html', {'form': form})

# Success view
def SuccessView(request):
    return render(request, 'success.html')
