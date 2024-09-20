import random
from Garrafa import Garrafa
from threading import Thread
import time


class Estados:
    TRANQUILO = 0
    BEBENDO = 1
    COM_SEDE = 2

class Filosofo(Thread):
    tempoBebendo = 1
    
    def __init__ (self, id, name, matrix, garrafas: list[Garrafa]):
        
        Thread.__init__(self)
        self.id = id
        self.name = name
        self.state = Estados.TRANQUILO
        self.garrafas = garrafas
        self.matrix = matrix
        self.garrafasPegues: list[Garrafa] = []
        self.contadorBebeu = 0
        
    def ehUltimo(self):
        return self.id == self.getN() - 1
        
    def run(self):
        while True:
            if self.state == Estados.BEBENDO:
                self.beber()
            elif self.state == Estados.COM_SEDE:
                self.comSede()
            else:
                self.tranquilo()
    
    def getVizinhos(self):
        vizinhos = []
        for i in range(len(self.matrix)):
            if self.matrix[i] == '1':
                vizinhos.append(i)
        return vizinhos
    
    def getN(self):
        return len(self.matrix)
    
    def getQntGarrafas(self):
        return min(2, random.randint(2, self.getN()))
    
   
    def beber(self):
        self.state = Estados.BEBENDO
        print(self.name + " está bebendo")
        time.sleep(self.tempoBebendo)
        
        for garrafa in self.garrafasPegues:
            garrafa.soltar(self.name)
        
        self.garrafasPegues = []
                
        self.state = Estados.TRANQUILO
        self.contadorBebeu += 1
        
    def tranquilo(self):
        tempoTranquilo = random.randint(0, 5)

        print(self.name + " está tranquilo por " + str(tempoTranquilo)+ " s")
        time.sleep(tempoTranquilo)
        self.state = Estados.COM_SEDE
        
    def comSede(self):
        print(self.name + ' está com sede')
        
        qntGarrafas = self.getQntGarrafas()
        possiveisGarrafas = []
                        
        for item in self.getVizinhos():
            possiveisGarrafas.append(self.garrafas[item])
        
        intencaoDePegarGarrafas = random.sample(possiveisGarrafas, qntGarrafas)
        
        print(self.name + " tentou pegar as garrafas " + str(self.getVizinhos()))
        

        if self.ehUltimo():
            intencaoDePegarGarrafas.reverse()
        
        
        for garrafa in intencaoDePegarGarrafas:
            pegou = garrafa.pegar(self.name)
            if pegou:
                 self.garrafasPegues.append(garrafa)
            else:
                for garrafa in self.garrafasPegues:
                    garrafa.soltar(self.name)
                self.garrafasPegues = []
                break
            
        if len(self.garrafasPegues) == qntGarrafas:
            self.state = Estados.BEBENDO
        

        
        
        
                            
        
      
