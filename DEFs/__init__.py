def continue_if(perg, *respp, separador=True):
    """
    :param perg: é a pergunta
    :param respp: opções de respostas (str)
    :param separador: True -> separa; False -> não separa
    :return: a resposta

    DESENVOLVEDOR: Silas B. Ferreira
    """

    while True:
        esta = 0
        repete = input(perg).upper()
        for r in respp:
            # print(r)
            if repete in r:
                esta = 1
            else:
                esta = 0
                # if len(repete) != 1:
        if esta == 0 or len(repete) != 1:
            if separador:
                print('-='*15)
            print(f'\033[1;33m{"Tente novamente":^30}\033[m')
            if separador:
                print('-='*15)
        else:
            return str(repete)


def intentativas(t, lslc):
    """
    :param t: 1: no fácil; 2: no difícil (recomendado)
    :param lslc: tamanho da palavra
    :return: vai ser retornado a quantidade de tentativas permitidas ao usuário
    """
    t = int(t)
    if t == 1:
        res = 4
    else:
        res = 2
    res *= lslc
    return res


def estatistica(total, certas):
    """
    :param total: as letras digitadas
    :param certas: letras necessárias a serem digitadas
    :return: estatística
    """
    for_counter_chutes = str(total).replace("['", '').replace("']", "").replace("',", "").replace("'", "")\
        .replace(' ', '')

    totd = len(total)
    dig_necessarios = len(certas)
    # print(f'Eu sou o totd: {totd} ----> eu sou o digseiqla: {dig_necessarios}')

    print('Você chutou as letras: ', end='')
    counter = {}
    for t in for_counter_chutes:
        # I found at studies
        counter.setdefault(t[0], 0)
        counter[t] = counter[t[0]] + 1
        # I found at studies
        # print(f'{t}', end='')
    print()
    i = 0
    for letter, v in counter.items():
        if letter in certas.replace(' ', ''):
            print('\033[1;34m', end='')
        print(f'{letter.upper()}', end='. ')
        print('\033[m', end='')

    print()

    counter_rights = {}
    print('\nPorém só precisava das: ', end='')
    for t in str(certas):
        counter_rights.setdefault(t[0], 0)
        counter_rights[t] = counter_rights[t[0]] + 1
    # Faz o counter_right
    for k, v in counter_rights.items():
        print(f'{v}', end='')
        for it in k:
            print(f'\033[1;34m{it.upper()}\033[m', end='. ')
    # DIDN'T HAVE NECESSITY the for loop above
    print(f'\nPara formar a palavra --> \033[1;31m{certas.replace(" ", "").upper()}\033[m')
    res = dig_necessarios / totd
    print('\n')
    # 10, 20
    # 50 %
    # 6, #15
    return f'{res * 100:.2f}%'
