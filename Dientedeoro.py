
while True:
    print("*"*30)
    print("\tEl Diente de Oro")
    print("*"*30)
    print("1. Cotizar")
    print("2. Renunciar")
    print("3. Salir ")
    while True:
        try:
            opc=int(input("Ingrese opción: "))
            if 0<opc<4:
                break
            else:
                print("ERROR! Ingrese opción válida")
        except ValueError:
            print("ERROR! Ingrese números No letras")
    if opc==1:
        p_carilla=250000
        p_implante=475000
        p_ortodoncia=800000
        desc_aux=0.15
        desc_admi=0.1
        desc_doc=0.05
        print("¿Es parte de DUOC?: ")
        print("1. Si\n2. No")
        while True:
            try:
                opcd=int(input("Ingrese opción: "))
                if 0<opcd<3:
                    break
                else:
                    print("ERROR! Ingrese opción válida")
            except ValueError:
                print("ERROR! Ingrese números No letras")
        if opcd==1:
            while True:
                try:
                    print("En que área trabaja: ")
                    print("1. Auxiliar\n2. Administrativo\n3. Docente")
                    trabajador=int(input("Ingrese opción: "))
                    if 0<trabajador<4:
                        break
                    else:
                        print("ERROR! Ingrese opción válida")
                except ValueError:
                    print("ERROR! Ingrese números No letras")
        print("Tratamiento\t\t|\tvalor")         #menu tratamientos
        print("-"*40)
        print(f"Carillas Porcelana\t|\t${p_carilla}")
        print(f"Implantes Dentales\t|\t${p_implante}")
        print(f"Ortodoncia Brackets\t|\t${p_ortodoncia}")
        print("-"*40)
        print("*Todos los tratamientos incluyen:")
        print("-Limpieza y destartraje\n-Aplicación de sellante\n-Aplicación de fluor")
        while True:
            try: 
                cant_ca=int(input("Cantidad de Carillas Porcelana que decea:  "))
                subtotal_ca=p_carilla*cant_ca
                if cant_ca<0:
                    print("ERROR! Escriba un número positivo")
                else:
                    break
            except ValueError:
                print("ERROR! Ingrese números No letras")    
        while True:
            try: 
                cant_im=int(input("Cantidad de Implantes Dentales que decea:  "))
                subtotal_im=p_implante*cant_im
                if cant_im<0:
                    print("ERROR! Escriba un número positivo")
                else:
                    break
            except ValueError:
                print("ERROR! Ingrese números No letras")    
        while True:
            try: 
                cant_or=int(input("Cantidad de Ortodoncia Brackets que decea:  "))
                subtotal_or=p_ortodoncia*cant_or
                if cant_or<0:
                    print("ERROR! Escriba un número positivo")
                else:
                    break
            except ValueError:
                print("ERROR! Ingrese números No letras")
        subtotal=subtotal_ca+subtotal_im+subtotal_or
        print("-"*50)
        print("\tCotización")
        print("-"*50)
        print(f"---> {cant_ca} tratamiento(s) Carillas Procelana ${subtotal_ca} ")
        print(f"---> {cant_im} tratamiento(s) Carillas Procelana ${subtotal_im} ")
        print(f"---> {cant_or} tratamiento(s) Carillas Procelana ${subtotal_or} ")
        print("-"*50)
        print(f"Subtotal\t\t ${subtotal}")
        if opcd==1:
            if trabajador==1:
                print(f"Descuento\t\t ${desc_aux}")
                total=subtotal-(subtotal*desc_aux)
                print("-"*50)
                print(f"Totall\t\t ${total}")
                cuotas=total/12
                print("-"*50)
                print(f"Son 12 cuotas de:\t\t ${cuotas}")
            elif trabajador==2:
                print(f"Descuento\t\t ${desc_admi}")
                total=subtotal-(subtotal*desc_admi)
                print("-"*50)
                print(f"Totall\t\t ${total}")
                cuotas=total/12
                print("-"*50)
                print(f"Son 12 cuotas de:\t\t ${cuotas}")
            else:
                print(f"Descuento\t\t ${desc_doc}")
                total=subtotal-(subtotal*desc_doc)
                print("-"*50)
                print(f"Totall\t\t ${total}")
                cuotas=total/12
                print("-"*50)
                print(f"Son 12 cuotas de:\t\t ${cuotas}")
        elif opcd==2:
            print(f"Descuento\t\t $0")
            print("-"*50)
            print(f"Total\t\t ${subtotal}")
            cuotas=subtotal/12
            print("-"*50)
            print(f"Son 12 cuotas de:\t\t ${cuotas}")
        print("")
        print("Sonría Bonito!!!")
    elif opc==2:
        total=0
        subtotal=0
    elif opc==3:
        print("Hasta Luego\nSonría Bonito!")
        break
                        