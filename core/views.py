from django.shortcuts import render
from django.http import HttpResponse

from .models import Preco, Posto


# Create your views here.
def home(request):
    # precos = Preco.objects.filter(combustivel=3).order_by('preco')

    precos = Preco.objects.raw(
        '''
        SELECT p.id, po.nome_fantasia, p.preco, po.localizacao, 
        po.bandeira, p.data_add from core_preco as p 
        INNER JOIN core_posto as po ON po.id = p.posto_id 
        INNER JOIN core_combustivel as c ON p.combustivel_id = c.id 
        WHERE c.id = %s GROUP BY po.id HAVING max(po.data_add) 
        order by p.preco''', [4]
    )

    context = {
        'precos': precos
    }

    return render(request, 'index.html', context=context)
