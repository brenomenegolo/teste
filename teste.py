#2
print( True and True)                      
print( 1 == 1 and 2 == 1)                  
print( "test" == "test")                   
print( 1 == 1 or 2 != 1)                  
print( True and 1 == 1)                    
print( False and 0 != 0)                   
print( True or 1 == 1)                     
print( "test" == "testing")                
print( 1 != 0 and 2 == 1)                 
print( "test" != "testing")           
print( "test" == 1)                    
print( not (True and False))            
print( not (1 == 1 and 0 != 1))           
print( not (10 == 1 or 1000 == 1000))     
print( not (1 != 10 or 3 == 4))           
print( not ("testing" == "testing" and "Zed" == "Cool Guy"))  
print( 1 == 1 and (not ("testing" == 1 or 1 == 0)))           
print( "chunky" == "bacon" and (not (3 == 4 or 3 == 3)))      
print( 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")))  

#2
numero = int(input("Digite um número: "))

if numero >= 0:
    print("Número positivo")
else:
    print("Número negativo")

#3

valor = float(input("Valor do empréstimo: "))
parcelas = int(input("Número de parcelas: "))
salario = float(input("Salário: "))

valor_parcela = valor / parcelas

if valor_parcela <= salario * 0.3:
    print("Empréstimo aprovado")
else:
    print("Empréstimo negado")

    numero = int(input("informe um numero:"))
 
if numero % 2 == 0:
    print("par")

else:
    print("impar")

#4

valor_da_hora = float(input("informe o valor da hora:"))
numero_de_horas_no_mes = float(input("informe o numero de horas trabalhadas no mês:"))
percentual_de_desconto_do_inss = float(input("informe o porcentual de desconto no INSS:"))

Salario_bruto = valor_da_hora * numero_de_horas_no_mes
desconto = Salario_bruto * (percentual_de_desconto_do_inss/100)
salario_liquido = Salario_bruto - desconto
print("salario bruto:", Salario_bruto)
print("salrio liquido:", salario_liquido)


a = float(input("informe um numero"))
b = float(input("informe um numero"))

if a > b:
    print("maior:", a)

else:
    print("maior:", b)


#5

prova_a = float(input("informe a nota na prova a"))
prova_b = float(input("informe a nota na prova b"))
prova_c = float(input("informe a nota na prova c"))

media= (prova_a*2 + prova_b*3 + prova_c*5) / 10
print("a média das 3 provas é:", media)

#6

nome_do_candidato = input("informe o nome do aluno")
prova_portugues = float(input("informe a nota na prova de portugues"))
prova_de_matematica = float(input("informe a nota na prova de matemática"))
prova_gerais = float(input("informe a nota na prova de conhecimento gerais"))

media= (prova_portugues + prova_de_mateática + prova_gerais) / 3

if media > 7 and prova_portugues <= 5 and prova_de_matematica <=5 and prova_gerais <= 5:
    print("aprovado")
else:
    print("reprovado")
