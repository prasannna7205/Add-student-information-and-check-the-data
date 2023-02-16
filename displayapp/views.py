from django.shortcuts import render
from .import forms
from displayapp.models import UserData

# Create your views here.
def student_view(request):
    form=forms.User()
    if request.method == 'POST':
        form=forms.User(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request, 'index.html', {'form': form})
def empdat(request):
    emp_list=UserData.objects.all()
    my_dict={'emp_list':emp_list}
    return render(request, 'show.html',context=my_dict)

