from lib.interface import *
from lib.arquivo import *
from lib.dado import *

nomeArquivo = 'cadastros.txt'
arquivoExiste(nomeArquivo)
tmn = 35

while True:
    try:
        titulo('CADASTRO DE USUÁRIO', corSimb=4)
        esc = opcoes('Cadastrar', 'Lista dos cadastros', 'Sair do programa', corNum=1, corLinha=3, tmn=tmn)
        print()
        # Cadastrar
        if esc == 1:
            titulo('Cadastrar', corSimb=3, tmn=tmn)

            nome = leiaNome('Digite o seu nome: ')
            idade = leiaIdade('Digite a sua idade: ')
            cadastrar(nomeArquivo, nome, idade, tmn=tmn)

        # Listar os cadastros
        elif esc == 2:
            titulo('Lista dos cadastros', corSimb=3, tmn=tmn)
            mostrarCadastro(nomeArquivo, tmn=tmn)

        # Sair do programa
        elif esc == 3:
            titulo('Saindo do programa...', corSimb=3, tmn=tmn)
            print(f'{cores[4]}{"-> Volte sempre! <-":^{tmn}}{cores[0]}')
            sleep(1)
            break

    except KeyboardInterrupt:
        msgErro('ERRO: O usuário interrompeu o programa.')
        titulo('Saindo do programa...', corSimb=3, tmn=tmn)
        print(f'{cores[4]}{"-> Volte sempre! <-":^{tmn}}{cores[0]}')
        sleep(1)
        break
