print('****SEJA BEM VINDO(A) AO APLICATIVO SWEET DRAEMS****')
print('***FAÇA O LOGIN PARA PODER PEDIR O DELIVERY***')
l=str(input("""FAZER O LOGIN?
1-SIM
2-NÃO
3-FAZER CADASTRO
"""))
a=0
k='Kelvy Corrêa'
b=0
c=''
lo='' 
import sys
import os
import getpass
def restart_program():
     python = sys.executable
     os.execl(python, python, * sys.argv)
if l=='1':
     while l=='1':
         user=str(input('DIGITE O NOME DE USUARIO: '))
         senha=getpass.getpass("DIGITE SUA SENHA: ")
         if (senha=='10112003' and (user=='Kelvy Corrêa')):
             a=1
             b=1
             print('LOGIN FEITO COM SUCESSO!')
             lo='1' 
             break
         elif (senha!= '10112003' and (user!='Kelvy Corrêa')):
             print('SENHA INVALIDA OU USUARIO INVALIDO')
             print("""*1-REFAZER LOGIN*
*2-PULAR LOGIN""")
             lg=str(input('QUER PROSSEGUI OU REFAZER O LOGIN? '))
             if lg=='1':
                 os.system("cls")
                 restart_program()
             elif lg=='2':
                 break   
elif l=='3':
     user=input(str('DIGITE SEU NOME DE CADASTRO: '))
     senha=getpass.getpass("DIGITE SUA SENHA PARA CADASTRAR ")
     email=str(input('DIGITE SEU EMAIL PARA RECEBER NOTICIAS SOBRE NÓS: '))
     telefone=str(input('DIGITE O SEU NÚMERO DE TELEFONE(COM DDD): '))
     lo='1'
     a=1
     b=1
elif l=='2':
     print('PULANDO LOGIN..')
else:
     print('COMANDO INVALIDO')
print("""========SWEET DREAMS======
***Obs: A entrega só será aceita caso o valor seja maior que R$12,00***
ENTREGAS DISPONIVEIS:
1 -Bala R$0,15
2 -Pirulito R$0,60
3 -barra de chocolate pequena R$1,50
4 -barra de chocolate grande R$3,00
5 -Salgado (kits de 100) R$20,00 (Venda somente por kits)
6 -Bolos de sabores R$13,00 a R$16,00
7 -Bolo de pote R$2,50
8 -Mousse(pote) sabores R$3,00
9 -Pudim (pote) R$3,50
10-Torta (pote) sabores R$3,50
11-Cupcake R$2,50
12-Lámen NÉJI R$8,00
====================
RECEITAS DISPONIVEIS:
====================
1-Bala gourmet de leite ninho
2-Barra de chocolate caseira
3-Bolos de varios sabores(com recheio)
4-Bolo de pote
5-Mouse
6-Pudim
7-Torta de maçã (especialidade)
8-Cupcake
9-Lámen NÉJI
===========================""")
val1=val2=val3=val4=val5=val6=val7=val8=val9=val10=val11=val12=0
quan1=quan2=quan3=quan4=quan5=quan6=quan7=quan8=quan9=quan10=quan11=quan12=0
des='S'
jus=''
recheio='' 
sabor=''
sabordr=''
pro=''
print("""*1-DELIVERY*
*2-CADERNO DE RECEITAS*""")
esco=int(input(''))
if (esco==1 and (lo=='1' and (a==1 and (b==1)))):
     while des=='s' or 'S':
         pro=str(input('DIGITE O NÚMERO DO PRODUTO: '))
         if pro=='1':
             quan1=int(input('DIGITE A QUANTIDADE: '))
             val1= 0.15 *quan1
         elif pro=='2':
             quan2=int(input('DIGITE A QUANTIDADE: '))
             val2= 0.60*quan2
         elif pro=='3':
             quan3=int(input('DIGITE A QUANTIDADE: '))
             val3= 1.50 * quan3
         elif pro=='4':
             quan4=int(input('DIGITE A QUANTIDADE:'))
             val4= 3.0 * quan4
         elif pro=='5':
             quan5=int(input('DIGITE A QUANTIDADE DE KITS: '))
             val5=20*quan5
         elif pro=='6':
             print("""=========================
OS SABORES SÃO:
*1-MORANGO*
*2-CHOCOLATE*
*3-COCO* 
*4-MARACUJA*
*5-ABACATE*
*6-DOCE DE LEITE*
*7-BRIGADEIRO*
*8-BEIJINHO*
=========================""")
             quan6=int(input('DIGITE A QUANTIDADE: '))
             sabor=str(input('DIGITE O SABOR(ES) DO(S) BOLO(S): '))
             print("""=========================
OS SABORES DOS RECHEIOS SÃO:
*1-CHOCOLATE*
*2-MORANGO*
*3-UVA*
*4-DOCE DE LEITE*
*5-BRIGADEIRO*
*6-MOUSSE DE MARACUJA*
*7-BEIJINHO*
*8-NOZES*
=========================""")
             recheio=str(input('DIGITE SE QUER RECHEIO:[S/N] '))
             val6=13.00*quan6
             if (recheio=='S') or (recheio=='s'): 
                 sabordr=str(input('DIGITE O SABOR(ES): '))
                 val6=(quan6*3)+val6
             elif (recheio=='N') or (recheio=='n'):
                 val6=13.00*quan6
             else:
                 print('NÃO ENTENDEMOS SUA DECISÃO')
                 val6=val6-val6
         elif pro=='7':             
             print("""=========================
OS SABORES SÃO:
*1-MORANGO*
*2-CHOCOLATE*
*3-COCO* 
*4-MARACUJA*
*5-ABACATE*
*6-DOCE DE LEITE*
*7-BRIGADEIRO*
*8-BEIJINHO*
=========================""")
             sabor=int(input('DIGITE O(S) SABOR(ES): '))
             quan7=int(input('DIGITE A QUANTIDADE: '))
             val7=2.50*quan7  
         elif pro=='8':
             print("""=========================
OS SABORES SÃO:
*1-MORANGO*
*2-CHOCOLATE* 
*3-MARACUJA*
*4-ABACATE*
*5-LIMÃO*
=========================""")
             sabor=int(input('DIGITE O(S) SABOR(ES): '))
             quan8=int(input('DIGITE A QUANTIDADE: '))
             val8=3.0*quan8
         elif pro=='9':
             quan9=int(input('DIGITE A QUANTIDADE DE FÁTIAS: '))
             val9=3.5*quan9
         elif pro=='10':
             print("""=========================
OS SABORES SÃO:
*1-MORANGO*
*2-CHOCOLATE*
*3-COCO* 
*4-MARACUJA*
*5-ABACATE*
*6-DOCE DE LEITE*
*7-BRIGADEIRO*
*8-BEIJINHO*
=========================""")
             sabor=int(input('DIGITE O(S) SABOR(ES): '))
             quan10=int(input('DIGITE A QUANTIDADE: '))
             val10=3.5*quan10
         elif pro=='11':
             print("""=========================
OS SABORES SÃO:
*1-MORANGO*
*2-CHOCOLATE*
*3-COCO* 
*4-MARACUJA*
*5-ABACATE*
*6-DOCE DE LEITE*
*7-BRIGADEIRO*
*8-BEIJINHO*
=========================""")
             sabor=int(input('DIGITE O(S) SABOR(ES): '))
             quan11=int(input('DIGITE A QUANTIDADE: '))
             val11=2.5*quan11
         elif pro=='12':
             print("""OS SABORES SÃO:
1-TONKOTSU
2-MISSÔ
3-SHIOYU""")
             sabor=int(input('CRIATURA SÁBIA, PROVIDA DE INTELIGÊNCIA, VOSSO INTELECTO É ALTO POR ESCOLHER TAL ALIMENTO PARA VUS ABASTECER, QUAL O SABOR VÓS ESCOLHERÁ?'))
             quan12=int(input('QUAL A QUANTIDADE QUE VOSSA SANTIDADE ESCOLHERÁ?'))
             val12=8.0*quan12
         else:
             print('não entendemos seu comando vamos recomeçar!!')
             continue         
         jus=str(input('QUER ADICIONAR ALGO MAIS À ENTREGA:[S/N]  '))
         if jus=='N':
             print(f'O VALOR TOTAL É R${val1+val2+val3+val4+val5+val6+val7+val8+val9+val10+val11+val12}')
             if (val1+val2+val3+val4+val5+val6+val7+val8+val9+val10+val11+val12)<=12.00:
                 print('VALOR INSUFICIÊNTE')
                 break
             h=str(input("""HORARIOS DISPONIVEIS A PARTIR DE 10:00 ATÉ 21:00
DIGITE A HORA DA ENTREGA: """))
             if h=='10:00' or '11:00' or '12:00' or '13:00' or '14:00' or '15:00' or '16:00' or '17:00' or '18:00' or '19:00' or '20:00' or '21:00':
                 print(f'SEU PEDIDO VAI SER ENTREGUE EM UM HORARIO MÉDIO DE {h}h , AGRADECEMOS PELA CONFIANÇA')
                 break
             elif h!='10:00' or '11:00' or '12:00' or '13:00' or '14:00' or '15:00' or '16:00' or '17:00' or '18:00' or '19:00' or '20:00' or '21:00':
                 print('HORARIO INVALIDO') 
             else:
                 print('DECISÃO INVALIDA')  
         elif jus=='S':
             continue
         elif jus=='s':
             continue
         elif jus=='n':
             print(f'O VALOR TOTAL É R${val1+val2+val3+val4+val5+val6+val7+val8+val9+val10+val11+val12}')
             if (val1+val2+val3+val4+val5+val6+val7+val8+val9+val10+val11+val12)<=12.00:
                 print('VALOR INSUFICIÊNTE')
                 break
             h=str(input("""HORARIOS DISPONIVEIS A PARTIR DE 10:00 ATÉ 21:00
DIGITE A HORA DA ENTREGA: """))
             if h=='10:00' or '11:00' or '12:00' or '13:00' or '14:00' or '15:00' or '16:00' or '17:00' or '18:00' or '19:00' or '20:00' or '21:00':
                 print(f'SEU PEDIDO VAI SER ENTREGUE EM UM HORARIO MÉDIO DE {h}h , AGRADECEMOS PELA CONFIANÇA')
                 break
             elif h!='10:00' or '11:00' or '12:00' or '13:00' or '14:00' or '15:00' or '16:00' or '17:00' or '18:00' or '19:00' or '20:00' or '21:00':
                 print('HORARIO INVALIDO')
             else:
                 print('DECISÃO INVALIDA') 
elif esco==2:
     while des=='s' or 'S':
         pro=str(input('DIGITE O NÚMERO DO PRODUTO QUE VOCÊ QUER A RECEITA: '))
         if pro=='1':
             print("""balas gourmet de leite ninho
=============
INGREDIENTES
=============
1 lata de leite condensado
1 xícara de chá de leite ninho
2 colheres de sopa de glucose de milho
1 colher de café de essência de baunilha
½ xícara de chá de leite ninho (para empanar)
========================================
COMO FAZER BALAS GOURMET DE LEITE NINHO
MODO DE PREPARO
========================================
Em uma panela, misture o leite condensado, o leite ninho, a glucose de milho e a essência de baunilha.
Leve ao fogo médio, mexendo sem parar até desgrudar do fundo da panela.
Quando desgrudar do fundo da panela, cozinhe, misturando sempre, por mais 8 minutos.
Desligue o fogo e transfira a massa para uma tigela untada com margarina.
Cubra com plástico filme bem rente à massa e espere esfriar completamente (em temperatura ambiente).
Depois de fria, transfira a massa para uma bancada untada com margarina.
Com uma faca untada com margarina, corte a massa em fatias de 2 cm.
Com as mãos untadas, enrole as fatias de massa, formando rolinhos.
Com uma tesoura untada com margarina, corte o rolinho em pedaços, formando as balas.
Passe as balas no leite ninho e sirva ou então guarde em potinhos ou saquinhos bem fechados, em temperatura ambiente. Assim as balas de leite ninho duram por até 15 dias!""")
         elif pro=='2':
             print("""
===============
INGREDIENTES
===============
1 xícara de leite
1 xícara de açucar
1 colher de sopa de manteiga
4 colheres de sopa de chocolate em pó
Manteiga para untar uma forma de alumínio
================
MODO DE PREPARO
================
Coloque todos os ingredientes em uma panela no fogo brando.
Fique mexendo com uma colher de pau sem parar.
Quando o leite começar a subir abaixe o fogo e continue mexendo.
Após o leite parar de subir e começar a engrossar e aparecer o fundo da panela, retire do fogo e bata com a colher de pau fora do fogo.
Despeje na forma de alumínio untada.
Quando estiver morna, passe a faca para quadricular. Comer frio.""")
         elif pro=='3':
             print("""OS SABORES SÃO:
*1-CHOCOLATE*
*2-COCO* 
*3-DOCE DE LEITE*
""")
             sabor=str(input('ESCOLHA O SABOR DO BOLO:'))
             if sabor=='1':
                 print("""===========
MASSA:
=============
4 ovos
4 colheres (sopa) de chocolate em pó
2 colheres (sopa) de manteiga
3 xícaras (chá) de farinha de trigo
2 xícaras (chá) de açúcar
2 colheres (sopa) de fermento
1 xícara (chá) de leite
==========
CALDA
==========
2 colheres (sopa) de manteiga
7 colheres (sopa) de chocolate em pó
2 latas de creme de leite com soro
3 colheres (sopa) de açúcar
=================
MODO DE PREPARO
=================
MASSA:
=================
Em um liquidificador adicione os ovos, o chocolate em pó, a manteiga, a farinha de trigo, o açúcar e o leite, depois bata por 5 minutos.

Adicione o fermento e misture com uma espátula delicadamente.

Em uma forma untada, despeje a massa e asse em forno médio (180 ºC) preaquecido por cerca de 40 minutos.
===============
CALDA:
===============
Em uma panela, aqueça a manteiga e misture o chocolate em pó até que esteja homogêneo.

Acrescente o creme de leite e misture bem até obter uma consistência cremosa.

Desligue o fogo e acrescente o açúcar. """)
             elif sabor=='2':
                 print("""===============
INGREDIENTES
===============
3 ovos
2 xícaras de açúcar
2 xícaras de farinha de trigo
1 xícara de leite
1/2 xícara de óleo
100 g de coco ralado
1 colher (sopa) de fermento em pó
=================
MODE DE PREPARO
=================
No liquidificador bata os ovos, açúcar, óleo e o leite
Adicione o coco ralado e a farinha de trigo e bata novamente para misturar
Desligue o liquidificador e coloque o fermento em pó; misture com uma colher manualmente
Despeje a massa em uma forma untada e enfarinhada
Leve ao forno médio por 45 minutos ou até espetar um palito e sair limpo
""")
             elif sabor=='4':
                 print("""==============
INGREDIENTES
===============
3 ovos
2 xícaras de açúcar
2 xícaras de farinha de trigo
1 xícara de leite
1/2 xícara de óleo
100 g de coco ralado
1 colher (sopa) de fermento em pó
================
MODO DE PREPARO
================
No liquidificador bata os ovos, açúcar, óleo e o leite
Adicione o coco ralado e a farinha de trigo e bata novamente para misturar
Desligue o liquidificador e coloque o fermento em pó; misture com uma colher manualmente
Despeje a massa em uma forma untada e enfarinhada
Leve ao forno médio por 45 minutos ou até espetar um palito e sair limpo
=======================
INFORMAÇÕES ADICIONAIS
=======================
Dica: para o bolo ficar mais fofo, peneire o trigo ao colocar na massa. Não abra o forno antes do tempo marcado.
""")
         elif pro=='4':
             print("""*1-COM RECHEIO DE COCO*
*2-COM RECHEIO DE BRIGADEIRO DE PAÇOCA*""")
             sabor=str(input('DIGITE O SABOR: '))
             if sabor=='1':
                 print("""Passo 1: A Massa
A base do bolo é simples mas precisa ser bem feita e com ingredientes de qualidade.

A massa que vou ensinar aqui é uma branca, leve e fofa.

Você pode também fazer diferentes tipos de massa, como chocolate, dependendo do sabor do seu bolo no pote.

Receita da Massa
Ingredientes
4 ovos
2 xícaras (chá) de açúcar
2 1⁄2 xícaras (chá) de farinha de trigo
1 colher (sopa) de manteiga sem sal
1 xícara (chá) de leite quente
1 pitada de sal
1 colher (sopa) cheia de fermento em pó
Preparo
Coloque na batedeira os ovos, o açúcar e bata até dissolver o açúcar e a mistura ficar clara.
Desligue a batedeira, adicione farinha de trigo aos poucos e misture até incorporar.
Dissolva a manteiga no leite quente e coloque na mistura.
Adicione o sal e o fermento em pó, bata novamente até ficar uma massa homogênea.
Coloque a massa em uma assadeira (30 cm X 25 cm) untada e leve para assar em forno médio pré-aquecido a 180°C por cerca de 30 minutos ou até dourar.
Tire do forno e deixe esfriar. Em seguida desenforme o bolo e com as mãos esfarele bem. Reserve.
 

Passo 2: O Recheio
receita bolo de pote

Tão importante quanto à massa para dar um sabor único ao doce, os recheios podem ser dos mais variados tipos (brigadeiro, abacaxi, Nutella, Leite Ninho, etc).

Então faça uma escolha que combine também com o tipo de massa.

Vou dar aqui 2 exemplos de receitas para recheio.

Receita do Recheio de Coco
Ingredientes
1 lata de leite condensado
300 ml de leite integral
100 g de coco ralado
1 colher (sobremesa) de manteiga sem sal
Preparo
Misture o leite condensado, leite, coco ralado e a manteiga até obter uma mistura homogênea.
Leve ao fogo médio e mexa até engrossar (cerca de 1o minutos)
Espere esfriar e use como recheio
Passo 3: A Montagem
Agora que está tudo pronto, a massa e o recheio, é hora de montar o bolo dentro do pote.

a. Pegue o pote que você escolheu

b. Coloque primeiro uma camada de recheio no fundo do pote

c. Agora por cima do recheio adicione uma camada da massa de bolo esfarelada

d. Molhe um pouco a massa com leite condensado.

e. Adicione mais uma camada do recheio e mais outra do bolo esfarelado. Você pode parar por aqui ou repetir o processo e fazer quantas camadas for necessário para completar o pote.

f. Coloque uma cobertura. Geralmente a cobertura é próprio recheio mas você pode incrementar e colocar o que preferir (granulado, pedaços de chocolate, chantilly, suspiros, etc""")
             elif sabor=='2':
                 print("""Passo 1: A Massa
A base do bolo é simples mas precisa ser bem feita e com ingredientes de qualidade.

A massa que vou ensinar aqui é uma branca, leve e fofa.

Você pode também fazer diferentes tipos de massa, como chocolate, dependendo do sabor do seu bolo no pote.

Receita da Massa
Ingredientes
4 ovos
2 xícaras (chá) de açúcar
2 1⁄2 xícaras (chá) de farinha de trigo
1 colher (sopa) de manteiga sem sal
1 xícara (chá) de leite quente
1 pitada de sal
1 colher (sopa) cheia de fermento em pó
Preparo
Coloque na batedeira os ovos, o açúcar e bata até dissolver o açúcar e a mistura ficar clara.
Desligue a batedeira, adicione farinha de trigo aos poucos e misture até incorporar.
Dissolva a manteiga no leite quente e coloque na mistura.
Adicione o sal e o fermento em pó, bata novamente até ficar uma massa homogênea.
Coloque a massa em uma assadeira (30 cm X 25 cm) untada e leve para assar em forno médio pré-aquecido a 180°C por cerca de 30 minutos ou até dourar.
Tire do forno e deixe esfriar. Em seguida desenforme o bolo e com as mãos esfarele bem. Reserve.
 

Passo 2: O Recheio
Receita do Recheio de Brigadeiro de Paçoca
Ingredientes
3 colheres (sopa) de manteiga sem sal derretida
3 latas de leite condensado
3 caixinhas de creme de leite
300g de paçoca esfarelada
Preparo
Em uma panela fora do fogo, coloque a manteiga derretida, o leite condensado, o creme de leite e a paçoca esfarelada e misture bem até que os ingredientes fiquem bem incorporados.
Leve ao fogo alto, mexendo sempre, até engrossar e ficar cremoso (cerca de 15 minutos).
Retire do fogo e deixe esfriar por 20 minutos para usar nos potes.
Passo 3: A Montagem
Agora que está tudo pronto, a massa e o recheio, é hora de montar o bolo dentro do pote.

a. Pegue o pote que você escolheu

b. Coloque primeiro uma camada de recheio no fundo do pote

c. Agora por cima do recheio adicione uma camada da massa de bolo esfarelada

d. Molhe um pouco a massa com leite condensado.

e. Adicione mais uma camada do recheio e mais outra do bolo esfarelado. Você pode parar por aqui ou repetir o processo e fazer quantas camadas for necessário para completar o pote.

f. Coloque uma cobertura. Geralmente a cobertura é próprio recheio mas você pode incrementar e colocar o que preferir (granulado, pedaços de chocolate, chantilly, suspiros, etc""")        
         elif pro=='5':
             print("""INGREDIENTES
Pudim:
1 lata de leite condensado
1 lata de leite (medida da lata de leite condensado)
3 ovos inteiros
Calda:
1 xícara (chá) de açúcar
1/2 xícara de água

MODO DE PREPARO
Pudim:

Primeiro, bata bem os ovos no liquidificador.

Acrescente o leite condensado e o leite, e bata novamente.

Calda:

Derreta o açúcar na panela até ficar moreno, acrescente a água e deixe engrossar.

Coloque em uma forma redonda e despeje a massa do pudim por cima.

Asse em forno médio por 45 minutos, com a assadeira redonda dentro de uma maior com água.

Espete um garfo para ver se está bem assado.

Deixe esfriar e desenforme.""")
         elif pro=='6':
             print("""Calda:
1 xícara (chá) de açúcar
Pudim:
1 Leite MOÇA® (lata ou caixinha)
2 medidas (da lata) de Leite Líquido NINHO Forti+ Integral
3 ovos
Calda:
1   Em uma panela de fundo largo, derreta o açúcar até ficar dourado.
2   Junte meia xícara (chá) de água quente e mexa com uma colher.
3   Deixe ferver até dissolver os torrões de açúcar e a calda engrossar.
4   Forre com a calda uma forma com furo central (19 cm de diâmetro) e reserve.
Pudim:
5   Em um liquidificador, bata todos os ingredientes do pudim e despeje na forma reservada.
6   Cubra com papel-alumínio e leve ao forno médio (180°C), em banho-maria, por cerca de 1 hora e 30 minutos.
7   Depois de frio, leve para gelar por cerca de 6 horas. Desenforme e sirva a seguir.
DICAS:
- É essencial que o pudim seja preparado em banho-maria para que asse de forma lenta e controlada, para atingir a textura ideal.
- Para que o seu pudim não forme furinhos, verifique se a temperatura do forno está regulada conforme indicação da receita. Leve a forma ao forno na grade superior, longe da chama.""")
         elif pro=='7':
             print("""SABORES DISPONIVEIS:
*1-MORANGO*
*2-MARACUJA*
*3-LIMÃO*
*4-ABACATE*""")
             sabor=str(input('DIGITE O SABOR: '))
             if sabor=='1': 
                 print("""INGREDIENTES
2 caixas de morangos frescos
1 lata de leite condensado
1 lata de creme de leite
1 caixinha de gelatina de morango

MODO DE PREPARO
Bata os morangos no liquidificador e acrescente aos poucos o leite condensado e o creme de leite.

Prepare a gelatina conforme as instruções do fabricante e acrescente à mistura do liquidificador.

Bata todos os ingredientes juntos por 2 minutos.

Despeje o creme em uma travessa de vidro e leve à geladeira por 1 hora.

Ao retirar da geladeira, decore a mousse com a outra caixa de morangos, mantendo-o na geladeira até o momento de servir.""")
             elif sabor=='2':
                 print("""INGREDIENTES
1 lata de leite condensado
1 lata de suco de maracujá (medida pela lata de leite condensado)
1 lata de creme de leite sem soro

MODO DE PREPARO
Em um liquidificador, bata o creme de leite, o leite condensado e o suco concentrado de maracujá.

Em uma tigela, despeje a mistura e leve à geladeira por, no mínimo, 4 horas.""")
             elif sabor=='3':
                 print("""INGREDIENTES
1 lata de leite condensado
1 lata de suco de maracujá (medida pela lata de leite condensado)
1 lata de creme de leite sem soro

MODO DE PREPARO
Em um liquidificador, bata o creme de leite, o leite condensado e o suco concentrado de maracujá.

Em uma tigela, despeje a mistura e leve à geladeira por, no mínimo, 4 horas.""")
             elif sabor=='4':
                 print("""INGREDIENTES
1 lata de leite condensado
1 lata de creme de leite
1 abacate

MODO DE PREPARO
Bata os 3 ingredientes no liquidificador e leve à geladeira.""")
         elif pro=='8':
             print("""INGREDIENTES
Massa:
150 g de manteiga gelada
meia xícara (chá) de açúcar
3 gemas
1 pitada de sal
1 colher (sopa) de essência de baunilha
1 e meia xícara (chá) de farinha de trigo (peneirada)
Creme:
1 e meia xícara (chá) de Leite Líquido NINHO Forti+ Integral
2 gemas
1 Leite MOÇA® (lata ou caixinha)
1 colher (sopa) de amido de milho
1 colher (chá) de essência de baunilha
Cobertura:
4 maçãs em fatias finas
3 colheres (sopa) de açúcar
1 colher (chá) de canela em pó
MODO DE PREPARO
Massa:
Em um recipiente, misture a manteiga com o açúcar e adicione as gemas, o sal e a essência baunilha. Misture bem com a ponta dos dedos até que os ingredientes estejam bem incorporados. Junte a farinha de trigo aos poucos até obter uma massa homogênea, que desgrude das mãos. Faça uma bola e enrole em filme plástico. Reserve em geladeira por cerca de 30 minutos.
Creme:
Em uma panela pequena, adicione o Leite NINHO, as gemas, o Leite MOÇA, o amido de milho e a essência de baunilha. Misture bem e leve ao fogo. Quando iniciar fervura abaixe o fogo e deixe cozinhar por cerca de 5 minutos. Reserve.
Cobertura:
Em um recipiente, misture as maçãs, o açúcar e a canela e reserve.
Montagem:
Em uma superfície polvilhada com farinha de trigo, abra a massa, com auxilio de um rolo, e cubra uma forma de aro removível (24 cm de diâmetro) e coloque o creme reservado no fundo. Distribua as maçãs reservadas em círculos, formando uma flor. Leve ao forno médio-alto (200°C), preaquecido, por cerca de 30 minutos ou até que a massa esteja dourada e as maçãs cozidas.""")
         elif pro=='9':
             print("""1-LOMBO SUÍNO
""")
             sab=str(input('ESCOLHA O SABOR: '))
             if sab=='1':
                 print("""Ingredientes
1 kg de carcaça de frango ou ossos de frango (caldo de frango)
1 unidade de cebola (caldo de frango)
1 unidade de cenoura (caldo de frango)
4 unidades de cogumelo tipo shiitake seco (caldo de frango)
1/3 pacote de alga marinha kombu (caldo de frango)
1 maço de cebolinha (caldo de frango)
1 cabeça de alho (caldo de frango)
30 gramas de gengibre (caldo de frango)
6 litros de água (caldo de frango)
1/4 unidade de cebola (caldo escuro)
1 dente de alho (caldo escuro)
2 maços de cebolinha (caldo escuro)
1 talo de salsão (pequeno) (caldo escuro)
1/2 xícara de saquê (caldo escuro)
1/4 xícara de shoyu (caldo escuro)
1/4 xícara de shoyu claro (caldo escuro)
1 colher de sopa de gergelim torrado (caldo escuro)
3 folhas de alga kombu pequenas (caldo escuro)
1 colher de chá de pimenta-do-reino (caldo escuro)
5 unidades de peixe seco (iriko) (caldo escuro)
1 pacote de katsuobushi (lascas de peixe seco) (caldo escuro)
2 colheres de sopa de vinagre de arroz (caldo escuro)
500 gramas de copa lombo (copa lombo)
100 ml de shoyu (copa lombo)
100 gramas de missoshiro (copa lombo)
100 ml de vinagre de arroz (copa lombo)
125 ml de saquê (copa lombo)
50 gramas de gengibre (copa lombo)
1 unidade de pimenta dedo-de-moça inteira (copa lombo)
1/4 pacote de algas wakame marinha (alga wakame)
500 ml de água (alga wakame)
2 unidades de ovo
600 gramas de massa de lámen (ou miojo)
10 fatias de massa de peixe cozida no vapor, comprada pronta (kamaboko)
a gosto de cebolinha quanto baste cortada na diagonal em 45 graus C
Modo de preparo
Preparo dos caldos
Após dourar a carcaça de frango a 200 graus C por 15 minutos no forno, coloque numa panela com os ingredientes do caldo de frango. Cubra com água e cozinhe em fogo baixo por três horas até obter um um litro de caldo denso e gelatinoso. Coe e adicione uma colher de shoyu. Misture todos os ingredientes do caldo escuro em uma panela e ferva por 40 minutos a 1 hora. Bata no liquidificador e peneire. Reserve. Este é um caldo base que dura bem na geladeira e pode ser congelado.
Rale o gengibre, faça um corte longitudinal na pimenta e misture todos os ingredientes da copa lombo. Em um recipiente esfregue o tempero na carne, coloque tudo num saco plástico e deixe descansar por no mínimo 12 horas. Retire e asse numa forma funda por 2 horas a 150 graus C coberta com papel alumínio. Retire, espere esfriar e coloque num pote fundo, cubra a carne com o caldo do assado e deixe na geladeira, normalmente da noite para o dia. Isso fará com que a carne assada fique mais suculenta. Retire com cuidado a banha que vai se formar no pote e reserve (será usada na finalização). Fatie finamente e reserve.
Hidrate a alga por aproximadamente 3 minutos em água. Não deixe mais do que isso senão a alga ficará muito mole. Após peneirar, adicione a água ao caldo de frango para dar um sabor extra no preparo. Reserve as algas.
Deixe o ovo em temperatura ambiente e cozinhe por 6 minutos em água. Retire e coloque num bowl com água e gelo para resfriar rapidamente. Descasque o ovo embaixo de água corrente, pois isso facilita o processo e evita de quebrar o ovo. Reserve. Ferva a água com um pouco de sal, adicione a massa e cozinhe entre 30 a 45 segundos. Retire e coloque direto no bowl que for servir.
Em cada tigela, coloque os ingredientes nessa ordem: 1 ponta de colher de banha, 1 colher de sopa de caldo escuro, massa, 5 fatias de porco, wakame a gosto, 5 fatias de kamaboko, um ovo cortado ao meio, cebolinha a gosto, caldo de frango para cobrir""")
         else:
             print('RECEITA INVALIDA ESCOLHA OUTRA')
             continue
         jus=str(input('QUER CONTINUAR VENDO ALGUMA RECEITA?(S/N) '))
         if jus=='s':
             continue
         elif jus=='N':
             print('AGRADECEMOS SUA VISITA')
             break
         elif jus=='S':
             continue
         elif jus=='n':
             print('AGRADECEMOS SUA VISITA')
             break
         else:
             print('NÃO ENTENDEMOS SUA DECISÃO..')
             continue
elif (esco==1 and (lo !='1')):
     print('É NECESSARIO FAZER O LOGIN PARA PEDIR O DELIVERY')
     lo=str(input("""QUER FAZER O LOGIN OU CADASTRO?
1-SIM
2-NÃO"""))
     if lo=='1':
         restart_program()
         os.system("cls")
     elif lo=='2':
         print('TENHA UM BOM-DIA!')
g=str(input(''))
