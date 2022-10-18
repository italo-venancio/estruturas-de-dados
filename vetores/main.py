from vetor import Vetor

def teste_vetor():
    vetor = Vetor()
    vetor.adicionar('Zac')
    vetor.adicionar('Vivi')
    vetor.adicionar('Lu')
    vetor.adicionar('Beto')
    vetor.adicionar('Joe')
    vetor.adicionar('Nick')
    vetor.adicionar('It')
    vetor.adicionar_posicao('Beto', 1)
    vetor.adicionar_posicao('Aline', 3)
    print(vetor)
    print(vetor.tamanho())
    vetor.remover()
    vetor.remover_posicao(5)
    vetor.remover_elemento('Zac')
    vetor.remover_todos_elementos('Beto')
    print(vetor)
    print(vetor.tamanho())
    print(vetor.pegar(2))
    print(vetor.contem('Nick'))
    print(vetor.contem('Olga'))

if __name__ == '__main__':
    teste_vetor()