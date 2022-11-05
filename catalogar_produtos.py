
print('****SISTEMA DE CATALOGO*****')
nome=str(input('DIGITE O NOME DO PRODUTO: '))
preco=float(input('DIGITE O PREÇO DO PRODUTO: '))
sabores=str(input('DIGITE O(S) SABOR(ES)(CASO TENHA UM SABOR UNICO DIGITE "PADRÃO"): '))
r=str(input('TEM RECHEIO? [S/N}] '))
if r=='S':
    recheio=str(input('DIGITE O(S) SABOR(ES): '))
    preco_r=float(input('DIGITE O PREÇO DO PRODUTO COM O RECHEIO(CASO NÃO MUDE DIGITE O PREÇO INICIAL): '))
    r='SIM'
elif r=='s':
    recheio=str(input('DIGITE O(S) SABOR(ES): '))
    preco_r=float(input('DIGITE O PREÇO DO PRODUTO COM O RECHEIO(CASO NÃO MUDE DIGITE O PREÇO INICIAL): '))
    r='SIM'
rec=str(input('POSSUI RECEITA?[S/N]: '))
if rec=='s':
    receita=str(input('DIGITE A RECEITA: '))
    rec='SIM'
elif rec=='S':
    receita=str(input('DIGITE A RECEITA: '))
    rec='SIM'
elif rec=='n' or rec=='N':
    rec='NÃO'
entrega=str(input('O PRODUTO PODERÁ SER ENTREGUE?[S/N]: '))
if entrega=='s' or entrega=='S':
    entrega='SIM'
elif entrega=='n' or entrega=='N':
    entrega='NÃO'
print('PRODUTO CADASTRADO COM SUCESSO!!')
if (r=='SIM' or r=='S'):
    print(f"""    NOME={nome}
    PREÇO={preco}R$
    SABOR(ES)={sabores}
    POSSUI RECHEIO={r}
    SABOR(ES) DO(S) RECHEIO(S)={recheio}
    PREÇO COM RECHEIO={preco_r}R$
    DISPONIVEL PARA ENTREGA={entrega}
    POSSUI RECEITA={rec}""")
elif (r=='n' or r=='N'):
    r='NÃO'
    print(f"""    NOME={nome}
    PREÇO={preco}R$
    SABOR(ES)={sabores}
    RECHEIO={r}
    DISPONIVEL PARA ENTREGA={entrega}
    POSSUI RECEITA={rec}""")
a=str(input('DIGITE "ENTER" PARA REINICIAR O PROGRAMA'))
