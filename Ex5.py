from modsim import *
import math
import random



def TC_inversa():
    tempo = round(-(50 * math.log(random.uniform(0.0, 1.0))) / 3, 0)
    if tempo == 0:
        return 1
    else:
        return tempo

tempo_total_da_fila = TimeSeries()
quantidade_de_atrasos = TimeSeries()

def simular(intervalo_onibus, quantidade_de_iteracoes):
    tempo_total_segundos_simulacao = 0
    for i in range(quantidade_de_iteracoes):
        aluno = State(esperando=0, onibus=0)
        tempo_total_da_fila_em_segundos = 0
        tempo_chegada_de_um_aluno = TC_inversa()

        while aluno.esperando < 60:
            if tempo_total_da_fila_em_segundos == tempo_chegada_de_um_aluno:
                aluno.esperando += 1
                tempo_chegada_de_um_aluno = tempo_total_da_fila_em_segundos + TC_inversa()
            tempo_total_da_fila_em_segundos = tempo_total_da_fila_em_segundos + 1

        tempo_total_da_fila[i] = tempo_total_da_fila_em_segundos / 60
        tempo_total_segundos_simulacao += tempo_total_da_fila_em_segundos

        if tempo_total_da_fila[i] < intervalo_onibus:
            quantidade_de_atrasos[i] = 1
        elif tempo_total_da_fila[i] > intervalo_onibus:
            quantidade_de_atrasos[i] = 0

    atrasos = 0

    for onibus_atrasado in quantidade_de_atrasos:
        if onibus_atrasado:
            atrasos = atrasos + 1

    print('tiveram {x} atrasos com intervalos de {y} minutos, para {z} alunos ao longo de {w} horas'.format(x=atrasos, y=intervalo_onibus, z=quantidade_de_iteracoes*60, w=tempo_total_segundos_simulacao/3600))


simular(15, 1000)
simular(12, 1000)
simular(10, 1000)


