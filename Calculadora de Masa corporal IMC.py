print("Calculadora de Índice de Masa Corporal (IMC)")

altura = input("¿Cuál es su altura en centímetros?: ")
altura_float = float(altura)

peso = input("¿Cuál es su peso en kg?: ")
peso_float = float(peso)

IMC = peso_float / (altura_float * altura_float)
print("Su IMC es:", round(IMC, 2))

if IMC < 18.5:
    print("Su peso es bajo. Se recomienda consultar con un médico o nutricionista.")
elif IMC < 25:
    print("¡Felicidades! Su peso es normal.")
elif IMC < 30:
    print("Su peso está en la categoría de sobrepeso. Se recomienda adoptar hábitos saludables para mantener un peso adecuado.")
elif IMC < 35:
    print("Su peso se encuentra en la categoría de obesidad moderada. Se recomienda consultar con un médico o nutricionista para desarrollar un plan para alcanzar un peso saludable.")
else:
    print("Su peso se encuentra en la categoría de obesidad severa. Es crucial buscar atención médica y seguir un plan personalizado para reducir el riesgo de problemas de salud graves.")
