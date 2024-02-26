import pandas as pd

periods = {
    '7:00 - 8:00': 'Preparação para o dia',
    '8:00 - 8:30': '1° Pomodoro de 25 minutos',
    '8:30 - 8:35': 'Pausa de 5 minutos',
    '8:35 - 9:00': '2° Pomodoro de 25 minutos',
    '9:00 - 9:05': 'Pausa de 5 minutos',
    '9:05 - 9:30': '3° Pomodoro de 25 minutos',
    '9:30 - 9:35': 'Pausa de 5 minutos',
    '9:35 - 10:00': '4° Pomodoro de 25 minutos',
    '10:00 - 10:30': 'Pausa longa de 30 minutos',
    '10:30 - 11:30': '5° Pomodoro de 25 minutos',
    '11:30 - 11:35': 'Pausa de 5 minutos',
    '11:35 - 12:00': '6° Pomodoro de 25 minutos'
}

dias_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira']
routine = pd.DataFrame(index=periods, columns=dias_semana)

for dia in dias_semana:
    for periodo, atividade in periods.items():
        routine.loc[periodo, dia] = atividade

routine.to_excel("StudyRoutine.xlsx")
