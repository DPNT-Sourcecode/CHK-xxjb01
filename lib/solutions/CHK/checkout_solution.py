

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

price_table = {'3A': 130, '5A': 200 ,'2B': 45, 'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40 }

def checkout(skus:str) -> int:

    result = 0
    count = {'3A':0, '5A':0, '2B':0, 'B': 0}
    discount = 0

    for item in skus:
        if item in price_table:
            if item in count.keys():
                count[item] += 1
            else:
                count[item] = 1
        else:
            result = -1

    if result != -1:

        for key, value in count.items():
            if key == 'A':
                print(f'value: {value}, remainder 5: {value % 5}, test: {value >= 4}')
                if value >= 4 and (value % 5 == 0 or (value - 1) % 5 == 0 or (value - 2) % 5 == 0 or (value - 3) % 5 == 0):

                    count['5A'] = int(value / 5)

                    if value % 5 == 3:
                        count['3A'] = int(value / 5)
                        count['A'] = 0
                    else:
                        count['A'] = value % 5

                elif value % 3 == 0 or (value - 1) % 3 == 0 :
                    count['3A'] = int(value / 3)
                    count['A'] = value % 3

            elif key == 'B':
                count['2B'] = int(value / 2)
                count['B'] = value % 2
            elif key == 'E':
                if value % 2 == 0:
                    if count['B'] > 0:
                        count['B'] = 0

                    if count['2B'] > 0:
                        count['2B'] = int(count['2B'] / 2)

        result = sum([price_table[item] * count[item] for item in count]) - discount * 30

    print(result)
    print(count)

    return result


