# Code made by Santiago Rodriguez Canovari

def calculate_SL_LONG(entry1, entry2, leverage, stopLossValue):
    SL = ((entry1 + entry2) / 2) - \
        (((entry1 + entry2) / 2) * stopLossValue / 100) / leverage
    result = calculateResult(SL, entry1, entry2, leverage)
    print(SL)
    return result


def calculate_SL_SHORT(entry1, entry2, leverage, stopLossValue):
    SL = ((entry1 + entry2) / 2) + \
        (((entry1 + entry2) / 2) * stopLossValue / 100) / leverage
    result = calculateResult(SL, entry1, entry2, leverage)
    print(SL)
    return result


def calculateResult(SL, entry1,  entry2, leverage):
    result = (((SL*100)/((entry1+entry2)/2))-100)*leverage
    return result


def get_values():
    entry1 = float(input("Enter Entry1: "))
    entry2 = float(input("Enter Entry2: "))
    leverage = float(input("Enter Leverage: "))
    stopLossValue = float(input(
        "At how much % you want your SL to be? For 25% write 25. For 22.67% write 22.67: "))
    return [entry1, entry2, leverage, stopLossValue]


def calculate():
    values = get_values()
    result = fun(values[0], values[1], values[2], values[3])
    print("SL percent: ", result, "%")
    option = int(
        input("Select an option: \n1) SHORT\n2) LONG\n0) Salir\n"))
    return option


option = int(input("Select an option: \n1) SHORT\n2) LONG\n0) Salir\n"))

while option != 0:
    if option == 1:
        fun = calculate_SL_SHORT
        print("Calculating fot SHORT")
        option = calculate()

    elif option == 2:
        fun = calculate_SL_LONG
        print("Calculating for LONG")
        option = calculate()
