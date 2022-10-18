from celula import Celula
 
class ListaLigada:
    def __init__(self):
        self.__primeira = None
        self.__ultima = None
        self.__total_de_elemetos = 0
   
    def adicionar_comeco(self, aluno):
        nova_celula = Celula()
        nova_celula.__elemento = aluno
        
        nova_celula.__proxima = self.__primeira #nova_celula aponta para primeira
        self.__primeira = nova_celula #nova_celula se torna a primeira da lista
 
        self.__total_de_elemetos += 1

    def adicionar_posicao(self, posicao, aluno):
        if posicao == 0:
            self.adicionar_comeco()
        elif posicao >= self.__total_de_elemetos:
            self.adicionar_fim(aluno)
        else:
            nova_celula = Celula() 
            nova_celula.__elemento = aluno

            anterior = self.__primeira

            for i in range(0, posicao-1):
                anterior = anterior.__proxima
        
            nova_celula.__proxima = anterior.__proxima #nova_celula aponta para a proxima da anterior
            anterior.__proxima = nova_celula #celula anterior aponta para nova_celula

            self.__total_de_elemetos += 1
 
    def adicionar_fim(self, aluno):
        if self.__total_de_elemetos == 0:
            self.adicionar_comeco(aluno)
        else:
            nova_celula = Celula()
            nova_celula.__elemento = aluno

            atual = self.__primeira

            while atual.__proxima != None:
                atual = atual.__proxima

            nova_celula.__proxima = atual.__proxima #nova_celula aponta para o fim da lista
            atual.__proxima = nova_celula #atual aponta para nova_celula
            
            self.__total_de_elemetos += 1
 
    def pegar(self, posicao):
        if posicao < 0 or posicao >= self.__total_de_elemetos:
            raise Exception("Posicao invalida!")
 
        atual = self.__primeira
 
        for i in range(0, posicao):
            atual = atual.__proxima
        return atual.__elemento
        
    def remover_comeco(self):
        self.__primeira = self.__primeira.__proxima #a proxima da primeira se torna a primeira da lista
        self.__total_de_elemetos -= 1

    def remover_posicao(self, posicao):
        if posicao == 0:
            self.remover_comeco()
        elif posicao == self.__total_de_elemetos-1:
            self.remover_fim(aluno)
        elif posicao >= self.__total_de_elemetos:
            print('Posicao invalida!')
        else:
            anterior = self.__primeira

            for i in range(0, posicao-1):
                anterior = anterior.__proxima

            anterior.__proxima = anterior.__proxima.__proxima #a celula anterior aponta para a proxima da celula removida
            
            self.__total_de_elemetos -= 1
        
    def remover_fim(self):
        atual = self.__primeira

        while atual.__proxima.__proxima != None: #loop para encontrar a penultima celula
            atual = atual.__proxima

        atual.__proxima = None #penultima celula aponta para None

        self.__total_de_elemetos -= 1
        
    def remover_elemento(self, aluno):
        atual = self.__primeira

        if atual.__elemento == aluno:
            self.remover_comeco()
        else:
            while atual.__proxima != None:
                if atual.__proxima.__elemento == aluno:
                    atual.__proxima = atual.__proxima.__proxima #celula atual aponta para a proxima da celula removida
                    break
                atual = atual.__proxima

            self.__total_de_elemetos -= 1

    def remover_todos_elementos(self, aluno):
        atual = self.__primeira

        if atual.__elemento == aluno:
            self.remover_comeco()
        
        while atual.__proxima != None:
            if atual.__proxima.__elemento == aluno:
                atual.__proxima = atual.__proxima.__proxima 
                self.__total_de_elemetos -= 1
            atual = atual.__proxima

        if atual.__proxima == self.__ultima and atual.__elemento == aluno:
            self.remover_fim()

    def contem(self, aluno):
        atual = self.__primeira
        while atual != None:
            if atual.__elemento == aluno:
                return True
            atual = atual.__proxima
        return False

    def tamanho(self):
        return self.__total_de_elemetos

    def __str__(self):
        string_final = '['
        atual = self.__primeira
 
        if atual != None:
            string_final = string_final + atual.__elemento
            atual = atual.__proxima
            while atual:
                string_final = string_final + ', ' + atual.__elemento
                atual = atual.__proxima
            
        string_final = string_final + ']'
        return string_final

        if self.__total_de_elemetos == 0:
            return '[]'
