from django.shortcuts import render
from django.http import HttpResponse

from .models import Preco, Posto, Combustivel


# Create your views here.

# def home(request):
#     return render(request, 'index.html', context=context)


def home(request):
    combustiveis = Combustivel.objects.filter(ativo=True)

    context = {
        'combustiveis': combustiveis,
    }

    return render(request, 'index.html', context=context)


def ranking(request):
    pk = request.GET['combustivel']

    precos = Preco.objects.raw(
        '''
        SELECT p.id, po.nome_fantasia, p.preco, po.localizacao, 
        po.bandeira, p.data_add from core_preco as p 
        INNER JOIN core_posto as po ON po.id = p.posto_id 
        INNER JOIN core_combustivel as c ON p.combustivel_id = c.id 
        WHERE c.id = %s AND po.ativo=true GROUP BY po.id HAVING max(p.data_add) 
        order by p.preco''', [pk]
    )

    context = {
        'precos': precos,
    }

    return render(request, 'ranking.html', context)
