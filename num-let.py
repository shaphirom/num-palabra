def convert_to_leter(num = None):
    d1 = {'0':'cero','1':'uno', '2':'dos', '3':'tres', '4':'cuatro', '5':'cinco', '6':'seis', '7':'siete', '8':'ocho', '9':'nueve'}

    d1_d1 = {'0':'','1':'once', '2':'doce', '3':'trece', '4':'catorce', '5':'quince', '6':'dieciseis', '7':'diecisiete', '8':'dieciocho', '9':'diecinueve'}
    d1_d2 = {'0':'','1':'veintiuno', '2':'veintidos', '3':'veintitres', '4':'veinticuatro', '5':'veinticinco', '6':'veintiseis', '7':'veinitisiete', '8':'veintiocho', '9':'veintinueve'}

    d2 = {'0':'','1':'diez', '2':'veinte', '3':'treinta', '4':'cuarenta', '5':'cincuenta', '6':'sesenta', '7':'setenta', '8':'ochenta', '9':'noventa'}

    d3 = {'0':'','1':'cien', '2':'docientos', '3':'trescientos', '4':'cuatrocientos', '5':'quinientos', '6':'seiscientos', '7':'setecientos', '8':'ochocientos', '9':'novecientos'}

    d0 = {'0':'','1':'','2':'mil', '3':'millones', '4':'billones', '5':'trillones', '6':'cuatrillones','7':"",'8':"",'9':""}


    #Conversion a una lista
    new_num = [ nx for nx in reversed(num)]

    #contador de cantidad de la lista
    dis_new = len(new_num)

    #lista compresas
    c_list = []
    
    while dis_new > 0:
        if dis_new %3 != 0:
            quitar = dis_new % 3
            c_list.append([new_num.pop() for x in range(quitar)])
            dis_new-=quitar
        else:
            c_list.append([new_num.pop() for x in range(3)])
            dis_new-=3

    #contador con nueva valor
    dis_new = len(c_list)



    #Iniciar escritura
    srr = ""
    
    for list_cent in c_list:
        cont = len(list_cent)
        
        for x in list_cent:

            if cont == 3:
                    if len(list_cent) == cont:
                        srr = f"{srr} {d3[x]}"
                        cont -=1
                        
                    else:
                        cont -=1

            elif cont == 2:
                valueMayor = int(x)
                cont -=1
            
            elif cont == 1:
                if 'valueMayor' in locals():
                    if valueMayor > 0 :
                        if valueMayor == 1:
                            if x != 0:
                                srr = f"{srr} {d1_d1[x]}"
                                cont -=1
                            else:
                                srr = f"{srr} {d2[x]}"
                                cont -=1

                        elif valueMayor == 2:
                            if x != 0:
                                srr = f"{srr} {d1_d2[x]}"
                                cont -=1
                            else:
                                srr = f"{srr} {d2[x]}"
                                cont -=1

                        else:
                            if x != 0:
                                srr = f"{srr} {d2[str(valueMayor)]} y {d1[x]}"
                                cont -=1
                            else:
                                srr = f"{srr} {d2[x]}"
                                cont -=1
                            
                    else:
                        srr = f"{srr} {d1[x]}"
                        cont -=1
                else:
                    srr = f"{srr} {d1[x]}"
                    cont -=1


            if cont == 0:
                if dis_new >= 2:
                    codigo = dis_new
                    srr = f"{srr} {d0[str(codigo)]}"

                    dis_new = dis_new - 1
            






        



    print(srr)





num = input("Ingrese un Numero\n")

try:
    nt = int(num)
    convert_to_leter(num)
except ValueError as e:
    print("Solo se aceptan numeros, Intente de Nuevo")
    pass

    

