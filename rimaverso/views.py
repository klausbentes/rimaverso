from django.shortcuts import render
from rimaverso.models import Dicionario

# Create your views here.

def index(request):
    return render(request, 'rimaverso/index.html')

def buscar(request):

    # Captura a palavra buscada pelo usuário
    if 'buscar' in request.GET:
        dicionario = Dicionario.objects.all().order_by('silabas')
        palavra_a_buscar = request.GET['buscar'].lower()

        try: #Se houver apenas uma palavra como a pesquisada
            rima_da_palavra = dicionario.get(palavra__iexact=palavra_a_buscar).rima
            print(rima_da_palavra)
            rimas_com_palavra = dicionario.filter(rima=rima_da_palavra)
            print(rimas_com_palavra)
            return render(request, 'rimaverso/buscar.html', {'palavra': palavra_a_buscar, 'rimas': rimas_com_palavra})
        
        # Se houver mais de uma pronúncia possível
        except Dicionario.MultipleObjectsReturned:
            print('Muitos!')
            opcoes = Dicionario.objects.all().filter(palavra__iexact=palavra_a_buscar)
            print(opcoes)
            return render(request, 'rimaverso/qual.html', {'palavra': palavra_a_buscar, 'opcoes': opcoes})

        # Se não houver nenhuma palavra como a pesquisada
        except Dicionario.DoesNotExist:
            print('Não achei, não!')
            return render(request, 'rimaverso/sem_resultado.html', {'palavra': palavra_a_buscar})

    else:
        print('Nada a fazer.')
        pass

def selecionar_pronuncia(request, palavra, pronuncia):
    dicionario = Dicionario.objects.all().order_by('silabas')
    # Busca as rimas com base na pronúncia selecionada
    palavra_selecionada = dicionario.get(palavra__iexact=palavra, pronuncia=pronuncia)
    rima_da_palavra = dicionario.get(pronuncia__iexact=pronuncia).rima
    rimas_com_palavra = dicionario.filter(rima=rima_da_palavra)
    return render(request, 'rimaverso/buscar.html', {'palavra': palavra_selecionada, 'rimas': rimas_com_palavra})