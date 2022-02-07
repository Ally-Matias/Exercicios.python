class aluno:
    pass
    def __init__(self):
        self.nome = input("")
        self.notas = []
        self.notas.append( float(input("")) )
        self.notas.append( float(input("")) )
        self.notas.append( float(input("")) )
    def media(self):
        return (self.notas[0] + self.notas[1] + self.notas[2]) / 3


class turma:
    pass
    def __init__(self):
        self.quant = int(input(""))
        self.alunos = []
        self.medias = []
        for c in range (self.quant):
            self.alunos.append( aluno() )
            self.medias.append( self.alunos[c].media() )

    def mostrarMedia(self):	
        mediaa = sum(self.medias)/len(self.medias)
        print ("{:.2f}".format (mediaa))
		

turma1 = turma()
turma1.mostrarMedia()
