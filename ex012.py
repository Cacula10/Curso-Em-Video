p = float(input('Informe o preço do produto R$: '))
d = p * 0.05
print("o Desconto é R$:{:.2f}, então o produto com desconto de 5% irá custar R${:.2f}".format(d, (p-d)))
