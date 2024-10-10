#5) Escreva um programa que inverta os caracteres de um string.

#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

def inverter_a_string(s): 
    inverta = ""
    for char in s: 
        inverta = char + inverta
    return inverta


string = input("Informe uma string para fazer a inversão ")
print(f"String invertida: {inverter_a_string(string)}")

#Se usarmos a string "Target" como entrada 
#teremos como saída "tegraT"
 