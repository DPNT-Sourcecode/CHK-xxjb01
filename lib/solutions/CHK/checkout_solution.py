

# noinspection PyUnusedLocal
# skus = unicode string
"""
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+

+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
+------+-------+------------------------+
"""
from tabnanny import check

price_table = {'3A': 130, '5A': 200 ,'2B': 45, 'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10}

def checkout(skus:str) -> int:

    result = 0
    count = {'A':0, '3A':0, '5A':0, '2B':0, 'B': 0, 'E': 0, 'F': 0}
    discount = 0

    def clear_a():
        value = count['A']
        if value >= 5:
            count['5A'] = int(value / 5)
            count['A'] = value - count['5A'] * 5

            if value % 5 >= 3:
                count['3A'] = int(value / 5)
                count['A'] = count['A'] - 3

        elif value < 5 and (value % 3 == 0 or (value - 1) % 3 == 0):
            count['3A'] = int(value / 3)
            count['A'] = value % 3


    def clear_e():
        value = count['E']
        if value > 1:
            counter = value
            if count['B'] > 0:
                while counter >= 0:
                    count['B'] -= 1
                    counter -= 2
                    if counter <= 1 or count['B'] == 0:
                        break

    def clear_b():
        value = count['B']
        count['2B'] = int(value / 2)
        count['B'] = value % 2

    def clear_f():
        nonlocal discount
        value = count['F']
        if value == 2:
            count['F'] += 1
            discount -= 10
        if value > 2:
            counter = count['F']
            print(counter)
            while counter >= 3:
                counter -= 3
                discount -= 10



    for item in skus:
        if item in price_table:
            if item in count.keys():
                count[item] += 1
            else:
                count[item] = 1
        else:
            result = -1

    if result != -1:

        clear_a()
        clear_e()
        clear_b()
        clear_f()

        result = sum([price_table[item] * count[item] for item in count]) + discount

    print(f'RESULT: {result}')
    print(f'COUNT: {count}')

    return result




