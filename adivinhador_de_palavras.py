def chamaIFdaDEF(u):
    """
    :param u: se a letra existe na palavra selecionada
    :return:
    """
    if u in selecionada:
        # print(f'UHUUUL, a letra {user} existe na palavra secreta.')
        print(' '*17, f'\033[1;42m!!!\033[m')
    else:
        # print(f'QUE PENA! a letra {user} NÃO EXISTE na palavra secreta.')
        print(' '*17, '\033[1;41m!!!\033[m')
        if len(digitadas) >= 1:
            digitadas.pop()


while True:
    # FAZER UM STARTER COM TANTAS VEZES

    from random import choice as cho
    import DEFs as vdfs
    # velha DEFs

    import scrapDefs as scrapfile

    # from DEFs import recordAUTO as rcauto

    selecionada = []
    # SORTEAR MAIS PALAVRAS, fazer um appendedor de palavras
    palavra_secreta = scrapfile.chamada()
    for p in palavra_secreta:
        selecionada.append(p)
    # input(palavra_secreta)

    selecionada = cho(palavra_secreta)
    # sorteia
    lenselecionada = len(selecionada)
    # print(selecionada)
    selecionada = selecionada.lower()

    validou = False
    digitadas = []
    total = []


    tentativasp1 = vdfs.continue_if('Selecione o modo: [1] FÁCIL, [2] SUGERIDO: ', str([1, 2, 3]))
    tentativas = vdfs.intentativas(tentativasp1, lenselecionada)

    cont = 1
    sectemporario = ''

    while cont <= int(tentativas):
        # Retornar a estatistica das tentativas
        print(f'Esta é sua {cont}º tentaiva de {tentativas}')
        user = input('Digite uma letra: ')
        user = user.lower()
        if user.__len__() != 1:
            print('Digite apenas uma única letra. '.upper(), end='')
            # user = input('Digite uma letra: ').upper()
        for i in range(97, 123):
            if user.lower() == chr(i).lower():
                validou = True
                break
            else:
                validou = False

        if user == chr(128) or user == chr(199) or validou:
            digitadas.append(user)
            chamaIFdaDEF(user)

            total.append(user)
            # break
        else:
            print('ERRO, digite uma letra. ')
            validou = False

        # Ç 128 # Ã 199
        sectemporario = ''
        if len(total) >= 1:
            for letra_sec in selecionada:
                if letra_sec in digitadas:
                    sectemporario += letra_sec
                else:
                    sectemporario += '*'
            if sectemporario == selecionada:
                print('\033[1;42m ' * 40, end='\033[m\n')
                print(f'{"Parabéns, você conseguiu!!!":~^40}')
                print(f'{sectemporario:~^40}'.upper())
                break

                #########
            print(f'{"POR ENQUANTO":.^40}')
            print(sectemporario)
            print(f'{"POR ENQUANTO":.^40}')
        cont += 1
    if sectemporario != selecionada:
        print('=' * 40)
        print(f'{"QUE PENA! VOCÊ NÃO CONSEGUIU!!":~^40}')
        print('=' * 40)
    # faz a lista da selecionada
    selected = ''
    for s in selecionada:
        selected += s
    # A ESTATÍSTICA TA AQUI
    est = vdfs.estatistica(total, selected)

    # TOTAL digitadas: total
    # CERTAS digitadas: digitadas

    print('\033[m='*60)
    print(f'{f"PORCENTAGEM DE ACERTOS -> {est}":▲^50}')
    print('='*60)
    # print('kkkkkkkkkkkkkk')
    error = [100.00, - float(est[:-1])]
    num_error = sum(error)

    print(f'{f"PORCENTAGEM de ERROS -> {num_error:.2f}%":▼^50}')
    print('=' * 60)
    # FAZER ESTATÍSTICA, PROMETO QUE É A ÚLTIMA PARTE KKK
    break

    # SORTEAR MAIS PALAVRAS, WHILE TRUE
    # FAZER UM APPENDEDOR DE PALAVRAS QUE APPENDE SE TIVER COM ESPAÇO
scrapfile.deletes_temporaries()