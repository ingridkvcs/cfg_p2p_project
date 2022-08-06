orders = (['Lending', 1000, 5.15],
          ['Borrowing', 1000, 4.8],
          ['Lending', 1000, 4.9],
          ['Borrowing', 1000, 5.1],
          ['Lending', 1500, 4.9],
          ['Borrowing', 2500, 5.1],
          ['Lending', 1500, 4.9],
          ['Borrowing', 500, 5.1],
          ['Lending', 500, 4.9],
          ['Borrowing', 10000, 6],
          ['Lending', 20000,4.1])

current_order = ['Borrowing',2500,4.9]


def Lending(Borrow_list,current_order,Lending_list):
    Total = current_order[1]
    for i in range(len(Borrow_list)):
        if current_order[2] == Borrow_list[i][2]:
            if Total > 0:
                Total -= Borrow_list[i][1]
                if Total >= 0:
                    Borrow_list[i][1] = 0
                else:
                    Borrow_list[i][1] = abs(Total)
                    break
    else:
        current_order[1] = Total
        Lending_list.append(current_order)

    Borrow_list = [value for value in Borrow_list if value[1] != 0]

    print(sorted(Borrow_list,key=lambda Borrow_list: Borrow_list[2]))
    print(sorted(Lending_list, key=lambda Lending_list: Lending_list[2]))


def Borrowing(Lending_list,current_order,Borrow_list):
    Total = current_order[1]
    for i in range(len(Lending_list)):
        if current_order[2] == Lending_list[i][2]:
            if Total > 0:
                Total -= Lending_list[i][1]
                if Total >= 0:
                    Lending_list[i][1] = 0
                else:
                    Lending_list[i][1] = abs(Total)
                    break
    else:
        current_order[1] = Total
        Borrow_list.append(current_order)
    Lending_list = [value for value in Lending_list if value[1] != 0]

    print(sorted(Lending_list, key=lambda Lending_list: Lending_list[2]))
    print(sorted(Borrow_list, key=lambda Borrow_list: Borrow_list[2]))

def order_matching(current_order,orders):
    Lend_list = []
    Borrow_list =[]
    for i in range(len(orders)):
        if orders[i][0] == 'Lending':
            Lend_list.append(orders[i])
        elif orders[i][0] =='Borrowing':
            Borrow_list.append(orders[i])

    if current_order[0] == 'Lending':
        Lending(Borrow_list,current_order,Lending_list)

    elif current_order[0] == 'Borrowing':
        Borrowing(Lend_list,current_order,Borrow_list)


order_matching(current_order,orders)



