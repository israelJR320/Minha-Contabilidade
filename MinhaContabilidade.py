print('\n')
print('\n' + '-*-' * 5 + 'Minha Contabilidade'.center(30) + 5 * '-*-')
while True:
    print('Menu Principal'.center(30))
    print('''
          [1] Gerenciar Lançamentos
          [2] Visualizar Relatórios
          [3] Orçamento Mensal
          [4] Planejamento e Metas
          [5] Despesas Com Cartão de Credito
          [0] Sair
        ''')
    select_mestre = int(input('Qual a opção: '))
    if select_mestre == 1:
        while True:
            print('Gerenciar Lançamentos'.center(30))
            print('''\n
                  [1] Adicionar Lançamento
                  [2] Editar Lançamento
                  [3] Excluir Lançamento
                  [4] Listar Lançamentos
                  [0] Retornar ao Menu Principal
                ''')
            select_menu1 = int(input('Qual opção: '))
            if select_menu1 == 1:
                print('Adicionar Lançamento')
            elif select_menu1 == 2:
                print('Editar lançamento')
            elif select_menu1 == 3:
                print('Excluir Lançamento')
            elif select_menu1 == 4:
                print('Listar Lançamentos')
            elif select_menu1 == 0:
                break
    elif select_mestre == 2:
        while True:
            print('Visualizar relatórios'.center(30))
            print('''
                  [1] Resumo Mensal
                  [2] Gastos por Categoria
                  [3] Gráfico simples
                  [0] Retornar ao Menu Principal
                ''')
            select_menu2 = int(input('Qual a opção: '))
            if select_menu2 == 1:
                print('Resumo Mensal')
            elif select_menu2 == 2:
                print('Gastos por Categoria')
            elif select_menu2 == 3:
                print('Gráfico Simples')
            elif select_menu2 == 0:
                break
    elif select_mestre == 3:
        while True:
            print('Orçamento Mensal'.center(30))
            print('''
                  [1] Definir Limite por Categoria
                  [2] Verificar Status do Orçamento
                  [3] Alertas
                  [0] Retornar ao Menu Principal
                ''')
            select_menu3 = int(input('Qual a opção: '))
            if select_menu3 == 1:
                print('Definir Limite por Categoria')
            elif select_menu3 == 2:
                print('Verificar Status do Orçamento')
            elif select_menu3 == 3:
                print('Alertas')
            elif select_menu3 == 0:
                break
    elif select_mestre == 4:
        while True:
            print('PLanejamento Mensal'.center(30))
            print('''
                  [1] Definir Meta de Economia Mensal
                  [2] Controlar Dívidas
                  [3] Reservas para Emergências
                  [0] Retornar ao Menu Principal
                ''')
            select_menu4 = int(input('Qual opção: '))
            if select_menu4 == 1:
                print("Definir Meta de Economia Mensal")
            elif select_menu4 == 2:
                print('Controlar Dívidas')
            elif select_menu4 == 3:
                print('Reservas Para Emergências')
            elif select_menu4 == 0:
                break
    elif select_mestre == 5:
        while True:
            print('Despesas com cartão de credito'.center(30))
            print('''
                  [1] Gerenciar Lançamentos
                  [2] Visualizar Relatórios
                  [3] Orçamento Mensal
                  [0] Retornar ao Menu Principal
                ''')
            select_menu5 = int(input('Qual opção: '))
            if select_menu5 == 1:
                while True:
                    print('Gerenciar Lançamentos'.center(30))
                    print('''
                        [1] Adicionar Lançamento
                        [2] Editar Lançamento
                        [3] Excluir lançamento
                        [4] Listar Lançamentos
                        [5] Despesas Com Cartão de Credito
                        [0] Retornar ao Menu Principal
                        ''')
                    select_menu1 = int(input('Qual opção: '))
                    if select_menu1 == 1:
                        print('Adicionar Lançamento')
                    elif select_menu1 == 2:
                        print('Editar lançamento')
                    elif select_menu1 == 3:
                        print('Excluir Lançamento')
                    elif select_menu1 == 4:
                        print('Listar Lançamentos')
                    elif select_menu1 == 0:
                        break
            elif select_menu5 == 2:
                while True:
                    print('Vizualizar relatórios'.center(30))
                    print('''
                        [1] Resumo Mensal
                        [2] Gastos por Categoria
                        [3] Gráfico simples
                        [0] Retornar ao Menu Principal
                        ''')
                    select_menu2 = int(input('Qual a opção: '))
                    if select_menu2 == 1:
                        print('Resumo Mensal')
                    elif select_menu2 == 2:
                        print('Gastos por Categoria')
                    elif select_menu2 == 3:
                        print('Gráfico Simples')
                    elif select_menu2 == 0:
                        break
            elif select_menu5 == 3:
                    while True:
                        print('Orçamento Mensal'.center(30))
                        print('''
                            [1] Deinir Limite por Categoria
                            [2] Verificar Status do Orçamento
                            [3] Alertas
                            [0] Retornar ao Menu Principal
                            ''')
                        select_menu3 = int(input('Qual a opção: '))
                        if select_menu3 == 1:
                            print('Definir Limite por Categoria')
                        elif select_menu3 == 2:
                            print('Verificar Status do Orçamento')
                        elif select_menu3 == 3:
                            print('Alertas')
                        elif select_menu3 == 0:
                            break
            elif select_menu5 == 0:
                break
    elif select_mestre == 0:
        break
print('Fim!')

# Israel Jr