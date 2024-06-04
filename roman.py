def int_to_roman(num):
    numeros_romanos = {
        1000: "M", 900: "CM", 500: "D", 400: "CD",
        100: "C", 90: "XC", 50: "L", 40: "XL",
        10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
    }
    
    resultado = ""
    for valor in numeros_romanos:
        while num >= valor:
            resultado += numeros_romanos[valor]
            num -= valor
    return resultado

def roman_to_int(romano):
    numeros_romanos = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    num = 0
    valor_anterior = 0
    
    for caracter in romano:
        valor = numeros_romanos[caracter]
        if valor > valor_anterior:
            num += valor - 2 * valor_anterior
        else:
            num += valor
        valor_anterior = valor
    
    return num

#TESTES INTEIRO PARA ROMANO
print('----- INTEIRO PARA ROMANO ----- \n')
print(int_to_roman(124))
print(int_to_roman(1231))
print(int_to_roman(9))

#TESTES ROMANO PARA INTEIRO
print('\n----- ROMANO PARA INTEIRO ----- \n')
print(roman_to_int('IX'))
print(roman_to_int('CLX'))
print(roman_to_int('CLX'))