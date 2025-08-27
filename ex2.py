# < 18
# >= 18 < 60
# >= 60
try:
    vIdade = input("Digite sua idade: ")
    vIdade = int(vIdade)
    if vIdade < 18:
        print("Jovem")
    elif vIdade >= 18 and vIdade < 60:
        print("Adulto")
    else:
        print("Idoso")
#except ValueError:
#    print("Por favor, digite um número inteiro válido.")
except Exception as e: # Catches any other exception
    print(f"An unexpected error occurred: {e}")

