pesos = input("Cuantos pesos colombianos tienes?: ")
pesos = float(pesos)
valor_dolar = 3875
dolares = str(round((pesos / valor_dolar), 2))

print(f"Tus {pesos} colombianos equivalen a {dolares} dolares.")