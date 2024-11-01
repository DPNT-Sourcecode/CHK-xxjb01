

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
                count['5A'] = int(value / 5)
                count['A'] = value % 5
                count['A'] = count['A'] % 3

                # count['5A'] = int(value / 3)
                # count['A'] = value % 3

                # if count['A'] % 5 != 0:
                #     div_num = 3
                #     count['3A'] = int(value / div_num)
                # else:
                #     div_num = 5
                #     count['5A'] = int(value / div_num)
                #
                # count['A'] = value % div_num

            elif key == 'B':
                count['2B'] = int(value / 2)
                count['B'] = value % 2
            elif key == 'E':
                if value % 2 == 0:
                    if 'B' in count.keys():
                        print(value / 2)
                        print(count['B'])
                        count['B'] -= int(value / 2) -1

        result = sum([price_table[item] * count[item] for item in count])

    print(count)

    return result

checkout('EE')