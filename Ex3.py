from modsim import *
import math
import random
import numpy as np
import matplotlib.pyplot as plt

TempoServico = {1: 20, 2: 50, 3: 23, 4: 17, 5: 38, 6: 26}

def simulacao():
    Celula = State(chegada=0, fila=0, ocupado=0, completo=0)

    t = 0
    serviceTime = TimeSeries()
    serviceTime[0] = 0
    chegadaTime = TimeSeries()
    chegadaTime[0] = 0
    terminoTime = TimeSeries()
    terminoTime[0] = 0

    rChegada = TimeSeries()
    rChegada[0] = Celula.chegada
    rFila = TimeSeries()
    rFila[0] = Celula.fila
    rOcupado = TimeSeries()
    rOcupado[0] = Celula.ocupado
    rCompleto = TimeSeries()
    rCompleto[0] = Celula.completo


    def chega_job():
        Celula.chegada += 1
        Celula.fila += 1
        serviceTime[Celula.chegada] = TempoServico[random.randint(1, 6)]
        chegadaTime[Celula.chegada] = t


    def processa_job():
        Celula.fila -= 1
        Celula.ocupado += 1


    def completa_job():
        Celula.completo += 1
        Celula.ocupado -= 1
        terminoTime[Celula.completo] = t


    while Celula.completo <= 24:
        if Celula.chegada <= 24:
            momento_proxima_chegada = (Celula.chegada + 1) * 30
        else:
            momento_proxima_chegada = math.inf

        if Celula.chegada == 0 or Celula.chegada == Celula.completo:  # vendo se não tem niguem pra chegar ou se tudo que chegou tá completo
            proximo_termino = math.inf
        else:
            proximo_termino = max([chegadaTime[Celula.completo + 1], terminoTime[Celula.completo]]) + serviceTime[Celula.completo + 1]

        step = [momento_proxima_chegada, proximo_termino]
        t = min(step)

        if np.argmin(step) == 0:
            chega_job()
            # print(Celula.chegada, Celula.fila, Celula.ocupado, Celula.completo)

        if np.argmin(step) == 1:
            completa_job()
            # print(Celula.chegada, Celula.fila, Celula.ocupado, Celula.completo)

        if Celula.ocupado == 0 and Celula.fila > 0:
            processa_job()

        rChegada[t] = Celula.chegada
        rFila[t] = Celula.fila
        rOcupado[t] = Celula.ocupado
        rCompleto[t] = Celula.completo

    return max(rFila)

fila_max_por_simulacao = []
index = 0

while index < 1000:
    #print(index)
    fila_max_por_simulacao.append(simulacao())
    index += 1

print(fila_max_por_simulacao)

plt.plot(fila_max_por_simulacao, label = 'fila MAX')
plt.show()

print(np.mean(fila_max_por_simulacao))
