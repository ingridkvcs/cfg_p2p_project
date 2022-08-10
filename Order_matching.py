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
          ['Lending', 20000, 4.1])

current_order = ['Lending', 5000, 5.1]

def lending(borrow_list, current_order, lending_list):
    Total = current_order[1]
    for i in range(len(borrow_list)):
        if current_order[2] == borrow_list[i][2]:
            if Total > 0:
                Total -= borrow_list[i][1]
                if Total >= 0:
                    borrow_list[i][1] = 0
                else:
                    borrow_list[i][1] = abs(Total)
                    break
    else:
        current_order[1] = Total
        lending_list.append(current_order)

    borrow_list = [value for value in borrow_list if value[1] != 0]

    return [(sorted(lending_list, key=lambda lending_list: lending_list[2])),
            (sorted(borrow_list, key=lambda borrow_list: borrow_list[2]))]


def borrowing(lending_list, current_order, borrow_list):
    Total = current_order[1]
    for i in range(len(lending_list)):
        if current_order[2] == lending_list[i][2]:
            if Total > 0:
                Total -= lending_list[i][1]
                if Total >= 0:
                    lending_list[i][1] = 0
                else:
                    lending_list[i][1] = abs(Total)
                    break
    else:
        current_order[1] = Total
        borrow_list.append(current_order)
    lending_list = [value for value in lending_list if value[1] != 0]

    return [(sorted(lending_list, key=lambda lending_list: lending_list[2])),
           (sorted(borrow_list, key=lambda borrow_list: borrow_list[2]))]


def order_matching(current_order, orders):
    lend_list = []
    borrow_list = []
    for i in range(len(orders)):
        if orders[i][0] == 'Lending':
            lend_list.append(orders[i])
        elif orders[i][0] == 'Borrowing':
            borrow_list.append(orders[i])

    if current_order[0] == 'Lending':
        return lending(borrow_list, current_order, lend_list)

    elif current_order[0] == 'Borrowing':
        return borrowing(lend_list, current_order, borrow_list)


print(order_matching(current_order, orders))


