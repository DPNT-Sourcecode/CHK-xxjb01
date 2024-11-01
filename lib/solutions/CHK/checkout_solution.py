

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
"""
from tabnanny import check

price_table = {'3A': 130,'2B': 45, 'A': 50, 'B': 30, 'C': 20, 'D': 15 }

def checkout(skus:str) -> int:

    result = 0
    count = {'3A':0, '2B':0}

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
                count['3A'] = int(value / 3)
                count['A'] = value % 3
            elif key == 'B':
                count['2B'] = int(value / 2)
                count['B'] = value % 2

        result = sum([price_table[item] * count[item] for item in count])

    return result
