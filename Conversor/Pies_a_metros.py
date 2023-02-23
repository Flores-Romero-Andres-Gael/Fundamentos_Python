while True:
    try:
        pies = float(input("Valor de los pies: "))
        metros = pies/3.2808
        print("metros = ", pies," / 3.2808 = ", metros ," m ")
        break
    except ValueError:
        print("Valor no admitido. Intente de nuevo...")