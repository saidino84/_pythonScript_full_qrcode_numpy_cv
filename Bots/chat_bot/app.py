import os

url_="https://repl.it/@saidino/ChatBotPythonBasics#main.py"

def processar_resposta(resposta,nome):

    if resposta=='1':
        print(f'''{os.linesep} {nome} na minha opiniao vale pena , isso pork Python é
         uma das linguagens que cresc no mundo e possui 
         salarios que vao desde R$2100,00 a ate R$10000,00 no Brasil, além de contar com uma média anula de R$85.000
         dolares nos EUA. {os.linesep}''')
    elif resposta=='2':
        print(f'''{os.linesep} {nome} Isso depende muito com o nivel de esforco, 
        dedicacao e busca diaria por vagas de cada individuo. Alguns conseguem com menos de 3 meses e
        outros com mais , tudo depende do quando vc ja sabe ou esta dissposto a correr atras para parender
          {os.linesep}''')
    elif resposta=='3':
        print(f"""{os.linesep} {nome} primeiro entrenda, ninguem vai te dizerou chegar
        magiamente um dia te dizer k vc esta BOM o suficiente para consiguir um emprego ou fzazer dinheiro com seu conhecimento,
        de programacao, seja em Python ou em qualker outra linguagem ou habilidade, vc simplesmente tem k 
        comecar dar a sua cara a tapa e comecar a plicar para oportunidade ou ate mesmo comecar a criar elas, desde
        o dia k vc ja domina os fundamentos de uma linguagem (se estamos falando do python, 
        recomendo aprender no minimo os 5 pilares de programacao.  {os.linesep}""")
    elif resposta=='4':
        print(f'''{os.linesep} {nome} Voce pode estudar atraves de videos gratuitos
         no Youtube, livros e sites de programacao, porem se buscar
         um lugar com suporte  1 a 1 , estrutura sequencial, projectos novos, todos os meses
         dos anos e um curso k vai te ensinar toda base e habilidades mais lucrativas k precisa para criar
         aplicacoes em python e estar pronto para o mercado, recomendo o cusrsodepython.net {os.linesep}''')
    else:
        print('''esse comando meu pai saidino me disse para calar !!!!\n digite apenas [1,2,3,4] ''')
def start():
    run =True
    nome=input('digite seu nome:')
    'pedir email'
    email=input('Digite seu e-mail')

    while(run):
        # apresentar o chat bot
        print('\033[32m Ola Bem vindo a Saidino Bots\033[m')
        print(os.linesep)
        # pedir nome
        
        'oferecer menu de opcoes'
        resposta= input(f'''Oque gostaria de saber hoje? {os.linesep}\t[1] vale a pena aprender Python?
        {os.linesep}\t[2] Quanto tempo leva para consiguor um emprego com Python?
        {os.linesep}\t[3] - Quando vou saber que estou BOM o suficiente para conseguir um emprego com python
        {os.linesep}\t
        [4] - Onde me recomenda estudar Python para conseguir um emprego ?{os.linesep}\t''')

        if len(nome)!=0 and len(nome)>2:
            processar_resposta(resposta,nome)
            if('n' in input("continuar ? [y/n]").upper()):
                print(f'Adeus {nome} !!!!')
                break

        else:
            print('fala serio isso nao é nome tente de novo')
            continue


if __name__ == '__main__':
    start()
    