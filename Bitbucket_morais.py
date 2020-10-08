from modsim import *
def simulacao():
    def TTF_inversa():
        tempos_falha = np.sort(812*np.random.weibull(2,1))
        return int(tempos_falha)

    def TR_inversa():
        tempo_reparo = np.random.uniform(4,45)
        return int(tempo_reparo)

    computador = State(quebrado = 0)
    def evento_1():
        computador.quebrado += 1
    def evento_2():
        computador.quebrado -= 1
    t = 0
    result = TimeSeries()
    result[0] = computador.quebrado
    while t <= 43800:
        if computador.quebrado == 0:
            tempo = TTF_inversa()
            evento_1()
            t = t + tempo
        result[t] = (computador.quebrado)
        if computador.quebrado == 1:
            tempo_reparo = TR_inversa()
            tempo_quebra = TTF_inversa()
            if tempo_reparo > tempo_quebra:
                evento_1()
            elif tempo_reparo < tempo_quebra:
                tempo = tempo_reparo
                evento_2()
                t = t + tempo
        result[t] = (computador.quebrado)
        if computador.quebrado == 2:
            tempo = tempo_reparo
            evento_2()
            t = t + tempo
        result[t] = (computador.quebrado)
    return (list(result))
def resultados():
    cont2 = 0
    for i in range(1000):
        cont = simulacao().count(2)
        cont2 = cont2 + cont
    return (cont2,cont2/1000)

print("foram encontrados {} defeitos, um percentual de {} %".format(resultados()[0],resultados()[1]))


