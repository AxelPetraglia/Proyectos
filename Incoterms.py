import time

def incoterms():
    calculo = int(input("¿Qué incoterm querés calcular?\n1 FOB, 2 FCA, 3 CIF, 4 CPT\n"))

    if calculo == 1: 
        valorEXW = int(input("Valor EXW: "))
        trans_int = int(input("Transporte Interno en origen: "))
        embalaje = int(input("Costo de embalaje: "))
        certificado = int(input("Costo de certificado: "))
        carga_buque = int(input("Costo de carga al buque: "))
        gastos_puerto = int(input("Costos de terminal portuaria de origen: "))
        
        TD = valorEXW + trans_int + embalaje + certificado + carga_buque + gastos_puerto

        reintegros = float(input("Reintegro: "))
        gastos = float(input("Retenciones de exportación: ")) + float(input("Despachante en origen: "))
        utilidad = float(input("Utilidad: "))

        divisor = 1 + reintegros - gastos - utilidad

        FOB = TD / divisor
        print("El TD es igual a: " + str(TD) + "\nEl divisor es igual a: " + str(divisor))
        print("El valor FOB es igual a: " + str(FOB))
        print("")
        time.sleep(0.6)
        incoterms()

    if calculo == 2:
        valorEXW = int(input("Valor EXW: "))
        trans_int = int(input("Transporte Interno en origen: "))
        embalaje = int(input("Costo de embalaje: "))
        certificado = int(input("Costo de certificado: "))
        
        TD = valorEXW + trans_int + embalaje + certificado

        reintegros = float(input("Reintegro: "))
        gastos = float(input("Retenciones de exportación: ")) + float(input("Despachante en origen: "))
        utilidad = float(input("Utilidad: "))

        divisor = 1 + reintegros - gastos - utilidad

        FCA = TD / divisor
        print("El TD es igual a: " + str(TD) + "\nEl divisor es igual a: " + str(divisor))
        print("El valor FCA es igual a: " + str(FCA))  
        print("")
        time.sleep(0.6)
        incoterms()  

    if calculo == 3: 
        FOB = float(input("Valor FOB: "))
        seguro = int(input("Costo del Seguro: "))
        transporte = int(input("Costo del Transporte Internacional: "))
        CIF = FOB + seguro + transporte
        print("El valor CIF es: " + str(CIF))
        print("")
        time.sleep(0.6)
        incoterms()
        
    if calculo == 4:
        FCA = float(input("Valor FCA: "))
        transporte = int(input("Costo del Transporte Internacional: "))

        CPT = FCA + transporte

        print("El valor CPT es: " + str(CPT))
        print("")
        time.sleep(0.6)
        incoterms()

#def modo_practicar():

incoterms()
