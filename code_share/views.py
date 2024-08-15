from django.shortcuts import render, redirect, get_object_or_404
from .models import Code
from .forms import CodeForm

def index(request):
    codes = Code.objects.all()
    return render(request, 'index.html', {'codes': codes})

def code_detail(request, code_id):
    code = get_object_or_404(Code, pk=code_id)
    return render(request, 'code_detail.html', {'code': code})

def upload_code(request):
    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CodeForm()
    return render(request, 'upload_code.html', {'form': form})
#cd code_portfolio
#source myvenv/Scripts/activate  