from Carro import Carro
from Hibrido import Hibrido

def main():
    cor = input("informe a cor do carro: ")
    modelo = input("informe o modelo do carro: ")
    ano = input("informe o ano do carro: ")
    a1 = Carro(cor, modelo, ano)
    a1.acelerar()
    a1.freiar()

if __name__ == "__main__":
    main()
