def conversion():
    hex1=input("Enter the hexadecimal number: ").split()

    data_element={
        "0":"0000",
        "1":"0001",
        "2":"0010",
        "3":"0011",
        "4":"0100",
        "5":"0101",
        "6":"0110",
        "7":"0111",
        "8":"1000",
        "9":"1001",
        "A":"1010",
        "B":"1011",
        "C":"1100",
        "D":"1101",
        "E":"1110",
        "F":"1111",
    }
    lista=""
    for i in range(len(hex1)):
        for key in  data_element:
            if hex1[i]==key:
                lista+=(data_element[key])
    print(lista)
conversion()
    

    

