from django.contrib import messages
from django.shortcuts import redirect, render
from contato.forms import FormContato

def contatoView(request):
    if request.method == 'GET':
        form = FormContato()
        context = {
            "form": form
        }
        return render(request, 'contato/contato.html', context=context)
    else:
        form = FormContato(request.POST)
        if form.is_valid():
            mensagem = form.save()
            form = FormContato()
            messages.success(request, 'Mensagem enviada com sucesso!')

        context = {
            "form": form
        }
        return render(request, 'contato/contato.html', context=context)
