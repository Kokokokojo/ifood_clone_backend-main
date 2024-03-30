
tarefas = []

while True:
    print('1 - criar tarefa')
    print('2 - remover tarefa')
    print('3 - marcar tarefa como concluido')

    opcao = int(input('Digite sua opção -> '))


    if opcao == 1:
        tarefa = input('tarefa para inserir: ')

        tarefas.append({'nome':tarefa, 'feito':False})

    if opcao == 2:
        tarefa = input('tarefa para remover: ')
        for x in tarefas:
            if x['nome'] == tarefa:
                tarefas.remove(x)
                break
            
    if opcao == 3:
        tarefa = input('tarefa para concluir: ')
        for x in tarefas:
            if x['nome'] == tarefa:
                x['feito'] = True
                break


    print(tarefas)