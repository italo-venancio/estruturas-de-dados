from listaLigada import ListaLigada

def teste_lista01():
    lista01 = ListaLigada()
    lista01.adicionar_comeco('Zac')
    lista01.adicionar_comeco('Vivi')
    lista01.adicionar_comeco('Lu')
    lista01.adicionar_comeco('Beto')
    lista01.adicionar_comeco('Joe')
    lista01.adicionar_fim('Nick')
    lista01.adicionar_fim('It')
    lista01.adicionar_posicao(5, 'Beto')
    lista01.adicionar_posicao(3, 'Aline')
    print(lista01)
    print(lista01.tamanho())
    lista01.remover_comeco()
    lista01.remover_posicao(5)
    lista01.remover_elemento('Zac')
    lista01.remover_todos_elementos('Beto')
    lista01.remover_fim()
    print(lista01)
    print(lista01.tamanho())
    print(lista01.pegar(2))
    print(lista01.contem('Nick'))
    print(lista01.contem('Olga'))

if __name__ == '__main__':
    teste_lista01()