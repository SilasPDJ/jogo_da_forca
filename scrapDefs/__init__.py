list_with_full_files = []


def nomear_arquivos():
    """
    :return: The file name of now
    """
    from datetime import datetime as dt
    dirof_today = dt.today()
    drftd = str(dirof_today).replace(':', '-').replace(' ', '_time')
    dirof_today = drftd[:-10]
    # print(dirof_today)
    return str(dirof_today)

# nomear_arquivos()


def scrap():
    from urllib.request import Request, urlopen

    words_dict = []

    req = Request('https://www.palabrasaleatorias.com/palavras-aleatorias.php?fs=10&fs2=1&Submit=Nova+palavra',
                  headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    name = nomear_arquivos()
    

    creator_dir()  # cria diretórios

    full_name = f'scrapDefs/scrapping-cholo/all/ALL-VALUES-{name}'
    list_with_full_files.append(f'ALL-VALUES-{name}')

    open_file = open(f'{full_name}.txt', 'w')

    # CREATE the full file
    content = str(webpage)
    # to chamando ele duas vezes provavelmente

    file_lines = content.split('\\n')
    for i in file_lines:
        open_file.write(i + '\n')

    open_file = open(f'{full_name}.txt', 'r')
    # for finding
    ler = open_file.readlines()
    open_file.close()
    # trying to find
    # input(type(ler))
    # input(pal)

    # Opens the file which will contain the MAIN scrap needed and GETTING it
    file = open(f'scrapDefs/scrapping-cholo/__READ__.txt', 'a+')
    for i in range(114, 170, 6):
        ler[i] = str(ler[i]).replace('</div>', '')
        # prepare the writer
        length = len(ler[i])
        escreve = ler[i][-length:-3]
        # Check characters
        # Just pickup without accent
        if all(c.isalpha() for c in escreve):
            file.write(str(escreve) + '\n')
            # print(escreve)
            words_dict.append(escreve)


def creator_dir():
    name = 'scrapping-cholo'
    import os
    os.chdir('scrapDefs')
    ls = os.getcwd()
    # print(ls)
    try:
        os.mkdir(name)
    except FileExistsError:
        # print(ls + '--> existe')
        ...
        try:
            os.mkdir(f'{name}/all')
        except FileExistsError:
            # print(ls + '2 ---> existe')
            ...
    os.chdir('../')
    # volta pra onde tava


def chamada():
    """
    :return: É a lista retornada ué no arquivo o-melhor-exD
    """
    lista_retornada = []
    scrap()
    file = open(f'scrapDefs/scrapping-cholo/__READ__.txt', 'r+')
    file = file.readlines()

    for f in file:
        lista_retornada.append(f[:-1])
    # print(lista_retornada)
    return lista_retornada


def deletes_temporaries():
    name = 'scrapDefs/scrapping-cholo/all'
    import os
    # print(os.getcwd() + 'SOU O TEMPORARIES 1111')
    os.chdir(name)
    # print(os.getcwd() + 'SOU O TEMPORARIES 2222')
    for files in list_with_full_files:
        os.remove(f'{files}.txt')
        # Arquivo removido com sucesso
        # Se eu quiser mover é só vir aqui
    # os.unlink('all')
    os.chdir('../../../')

    # print(os.getcwd() + 'SOU O TEMPORARIES 3333')
#
