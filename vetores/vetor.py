class Vetor:
    def __init__(self):
        self.__alunos = [None] * 100
        self.__total_de_alunos = 0
 
    def adicionar(self, aluno):
        self.__alunos[self.__total_de_alunos] = aluno
        self.__total_de_alunos += 1
 
    def adicionar_posicao(self, aluno, posicao):
        if posicao > self.__total_de_alunos:
            print("Posicao invalida!")
        else:
            index = self.__total_de_alunos
            while index >= posicao: # loop que se inicia no fim da lista
                
                if index > posicao:
                    self.__alunos[index+1] = self.__alunos[index] # os itens sao "empurrados" para a direita para poder adicionar um novo item  

                elif index == posicao:
                    self.__alunos[index+1] = self.__alunos[index]
                    self.__alunos[index] = aluno # adicionando o novo item 
                index -= 1
            self.__total_de_alunos += 1 

    def pegar(self, posicao):
        if self.__alunos[posicao] == None:
            msg = 'Erro'
            return msg
        else:
            return self.__alunos[posicao]
 
    def remover(self):
        self.__alunos[self.__total_de_alunos-1] = None
        self.__total_de_alunos -= 1

    def remover_posicao(self, posicao):
        if posicao > self.__total_de_alunos:
            print("Posicao invalida!")
        else:
            index = 0
            while index <= self.__total_de_alunos: 
                if index >= posicao: # a partir da posicao do item removido
                    self.__alunos[index] = self.__alunos[index+1] # cada posicao recebe o item seguinte   
                index += 1
            self.__total_de_alunos -= 1

    def remover_elemento(self, aluno):
        if self.contem(aluno) == False:
            print("Nao contem o elemento!")
        else:
            index = 0
            while index <= self.__total_de_alunos:
                if self.__alunos[index] == aluno:
                    self.remover_posicao(index)
                    break
                index += 1
            
    def remover_todos_elementos(self, aluno):    
        if self.contem(aluno) == False:
            print("Nao contem o elemento!")
        else:
            index = 0
            while index <= self.__total_de_alunos:
                if self.__alunos[index] == aluno:
                    self.remover_posicao(index)
                index += 1
 
    def contem(self, aluno):
        for index in range(self.__total_de_alunos):
            if self.__alunos[index] == aluno:
                return True
           
        return False
 
    def tamanho(self):
        return self.__total_de_alunos
 
    def __str__(self):
        #return self.__alunos
        ret = ' '.join(str(elemento) for elemento in self.__alunos)
        return ret

