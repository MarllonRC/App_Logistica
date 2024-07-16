print("Bem vindo a loja do Marllon Rafael LTDA")
valor_produto =  float(input("Entre com o valor do produto desejado: "))
qtd_produto = int(input("Entre com a quantidade do produto desejado: "))
desconto_produto = 0


#inicio fixação para desconto com base na quantiade de produto
if qtd_produto <=9:
  desconto_produto = 0.00
elif 10 <= qtd_produto < 100:
  desconto_produto = 0.05
elif 100 <= qtd_produto <= 999:
  desconto_produto = 0.10
else:
  desconto_produto = 0.15
#Fim fixação para desconto com base na quantiade de produto


#Inicio de calculo de desconto no valor do produto
total_sem_desconto = valor_produto * qtd_produto
print("O valor total sem desconto é de: R$ {:.2f}".format(total_sem_desconto))
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto_produto #Calculo para aplicação de desconto
print("O valor total com desconto é de: R$ {:.2f}".format(total_com_desconto))
#Fim de calculo de desconto no valor do produto
