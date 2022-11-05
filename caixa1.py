print('**** SISTEMA DE ENTRADA E SAÍDA DE FINANCEIRA ****')
print("""1 -Bala R$0,15                       | 11-Cupcake R$2,50
2 -Pirulito R$0,60                   | 12-Lámen NÉJI R$8,00
3 -barra de chocolate pequena R$1,50 | 13-Café R$2,00
4 -barra de chocolate grande R$3,00  | 14-Pão de mel R$3,00
5 -Salgado (kits de 100) R$20,00     | 15-Donuts R$4,00 
6 -Bolos de sabores R$13,00 a R$16,00| 16-Bolinhos de Chuva R$3,00 
7 -Bolo de pote R$2,50               | 17-Panqueca R$3,25
8 -Mousse fatia de sabores R$3,00    | 18-Bomba de Chocolate R$ 3,00    
9 -Pudim fatia R$3,50                | 19-Sacole Gourmet R$2,00
10-Fatia torta sabores R$3,50        | 20-Waffles R$4,00
""")
def temp():
     time.sleep(5)
val1=val2=val3=val4=val5=val6=val7=val8=val9=val10=val11=val12=val13=val14=val15=val16=val17=val18=val19=val20=0
quan1=quan2=quan3=quan4=quan5=quan6=quan7=quan8=quan9=quan10=quan11=quan12=quan13=quan14=quan15=quan16=quan17=quan18=quan19=quan20=0
des='S'
jus=''
recheio='' 
sabor=''
sabordr=''
pro=''
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
    elif pro=='13':
        acom=str('QUER ACOMPANHAMENTO [S/N]: ')
        if acom=='S':
            print("""OS ACOMPANHAMENTOS SÃO
*1-LEITE*
*2-CREME*
*3-ACHOCOLATADO*
*4-BAUNILHA*""")
            des2=str(input('QUAL ACOMPANHAMENTO O CLIENTE QUER: '))
            quan13=int(input('QUAL A QUANTIDADE DO PRODUTO: '))
            val13=2*quan13
        elif acom=='N':
            quan13=int(input('QUAL A QUANTIDADE DO PRODUTO: '))
            val13=2*quan13
        elif acom=='s':
            print("""OS ACOMPANHAMENTOS SÃO
*1-LEITE*
*2-CREME*
*3-ACHOCOLATADO*
*4-BAUNILHA*""")
            des2=str(input('QUAL ACOMPANHAMENTO O CLIENTE QUER: '))
            quan13=int(input('QUAL A QUANTIDADE DO PRODUTO: '))
            val13=2*quan13
        elif acom=='n':
            quan13=int(input('QUAL A QUANTIDADE DO PRODUTO: '))
            val13=2*quan13
    elif pro=='14':
        quan14=int(input('DIGITE A QUANTIDADE DO PRODUTO: '))
        val14=quan14*3.25
    elif pro=='15':
        print("""OS ACOMPANHAMENTOS SÃO:
1-CHOCOLATE
2-DECE DE LEITE
3-AÇÚCAR DE CONFEITEIRO
4-GRANULADO
5-CALDA DE CHOCOLATE
6-CANELA""")
        acom=input('O CLIENTE QUER ACOMPANHAMENTO [S/N] ')
        if acom=='S':
            des2=input('QUAL ACOMPANHAMENTO O CLIENTE QUER: ')
            if des2=='1':
                 quan15=int(input('DIGITE A QUANTIDADE DO PRODUTO: '))
                 val15=quan15*(4+2)
            elif des2=='2':
                quan15=int(input('DIGITE A QUANTIDADE DO PRODUTO: '))
                val15=quan15*(4+2)
            elif des2=='3':
                quan15=int(input('DIGITE A QUANTIDADE DO PRODUTO: '))
                val15=quan15*(4+0.25)
            elif des2=='4':
                quan15=int(input('DIGITE A QUANTIDADE DO PRODUTO: '))
                val15=quan15*4
            elif des2=='5':
                quan15=int(input('DIGITE A QUANTIDADE DO PRODUTO: '))
                val15=quan15*(4+0.25)
            elif des2=='6':
                quan15=int(input('DIGITE A QUANTIDADE DO PRODUTO: '))
                val15=quan15*4
        elif acom=='s':
            des2=str(input('QUAL ACOMPANHAMENTO O CLIENTE QUER: '))
            if des2=='1':
                 quan15=int(input('DIGITE A QUANTIDADE DO PRODUTO: '))
                 val15=quan15*(4+2)
            elif des2=='2':
                quan15=int(input('DIGITE A QUANTIDADE DO PRODUTO: '))
                val15=quan15*(4+2)
            elif des2=='3':
                quan15=int(input('DIGITE A QUANTIDADE DO PRODUTO: '))
                val15=quan15*(4+0.25)
            elif des2=='4':
                quan15=int(input('DIGITE A QUANTIDADE DO PRODUTO: '))
                val15=quan15*4
            elif des2=='5':
                quan15=int(input('DIGITE A QUANTIDADE DO PRODUTO: '))
                val15=quan15*(4+0.25)
            elif des2=='6':
                quan15=int(input('DIGITE A QUANTIDADE DO PRODUTO: '))
                val15=quan15*4
        elif acom=='N':
            quan15=int(input('DIGITE A QUANTIDADE DO PRODUTO: '))
            val15=quan15*4
        elif acom=='n':
            quan15=int(input('DIGITE A QUANTIDADE DO PRODUTO: '))
            val15=quan15*4    
    elif pro=='16':
        quan16=int(input('DIGITE A QUANTIDADE DO PRODUTO: '))
        val16=quan16*3
    elif pro=='17':
        quan15=int(input('DIGITE A QUANTIDADE DO PRODUTO: '))
        val17=quan17*3.25
    elif pro=='18':
        quan18=int(input('DIGITE A QUANTIDADE DO PRODUTO: '))
        val18=quan18*3
    elif pro=='19':
        quan19=int(input('DIGITE A QUANTIDADE DO PRODUTO: '))
        val19=quan19*2
        print('INSTRUA O CLIENTE PARA VER OS SABORES COM O(A) BALCONISTA')
    elif pro=='20':
        print("""OS ACOMPANHAMENTOS SÃO:
1-CALDA DE CARAMELO
2-CHANTILLY
3-FRUTAS VERMELHAS
4-MANTEIGA
5-DOCE DE LEITE
6-BANANA
7-SORVETE
8-BACON""")
        des2=str(input('QUAL ACOMPANHAMENTO O CLIENTE QUER: '))
        if acom=='1':
            quan20=int(input('DIGITE A QUANTIDADE DO PRODUTO: '))
            val20=quan20*4
        elif acom=='2':
            quan20=int(input('DIGITE A QUANTIDADE DO PRODUTO: '))
            v19al20=quan20*4
        elif acom=='3':
            quan20=int(input('DIGITE A QUANTIDADE DO PRODUTO: '))
            val20=quan20*(4+0.75)
        elif acom=='4':
            quan20=int(input('DIGITE A QUANTIDADE DO PRODUTO: '))
            val20=quan20*4
        elif acom=='5':
            quan20=int(input('DIGITE A QUANTIDADE DO PRODUTO: '))
            val20=quan20*(4+0.5)
        elif acom=='6':
            val20=quan20*4
        elif acom=='7':
            quan20=int(input('DIGITE A QUANTIDADE DO PRODUTO: '))
            val20=quan20*(4+1.25)
        elif acom=='8':
            quan20=int(input('DIGITE A QUANTIDADE DO PRODUTO: '))
            val20=quan20*(4+1)
    else:
        print('não entendemos seu comando vamos recomeçar!!')
        restart_program()
    print(f'VALOR DA COMPRA NESSE MOMENTO É R${val1+val2+val3+val4+val5+val6+val7+val8+val9+val10+val11+val12+val13+val14+val15+val16+val17+val18+val19+val20}')
    jus=str(input('QUER ADICIONAR ALGO MAIS À COMPRA:[S/N]  '))
    if jus=='N':
        break   
    elif jus=='S':
        continue
    elif jus=='s':
        continue
    elif jus=='n':
        break
print(f'O VALOR TOTAL É R${val1+val2+val3+val4+val5+val6+val7+val8+val9+val10+val11+val12+val13+val14+val15+val16+val17+val18+val19+val20}')        
print("""*1-CARTÃO*
*2-DINHEIRO*
""")
pag=str(input('FORMA DE PAGAMENTO: '))
if pag=='1':
     modo=str(input("""CRÉDITO OU DÉBITO
1-CRÉDITO
2-DÉBITO
"""))
     print('AGUARDANDO RECEBER CONFIRMAÇÃO DE PAGAMENTO...')
     time.sleep(5)
     print('TRANSAÇÃO APROVADA')
elif pag=='2':
    re=float(input('QUANTO O CLIENTE PAGOU: '))
    re2=re-(val1+val2+val3+val4+val5+val6+val7+val8+val9+val10+val11+val12+val13+val14+val15+val16+val17+val18+val19+val20)
    print(f'O VALOR TOTAL DO TROCO É R${re2}')
else:
    print('FORMA DE PAGAMENTO INVALIDA')
w=input('')