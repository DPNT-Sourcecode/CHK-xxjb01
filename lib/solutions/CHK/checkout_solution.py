

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
price_table = {'3A': 130,'2B': 45, 'A': 50, 'B': 30, 'C': 20, 'D': 15 }

def checkout(skus:str) -> int:

    result = 0
    count = {}

    for item in skus:
        if item in price_table:
            if item in count.keys():
                if item == 'A' and count[item] == 3:
                    if count['3A']:
                        count['3A'] += 1
                    else:
                        count['3A'] = 1
                    count['A'] = 0
                elif item == 'B' and count[item] == 2:
                    if count['2B']:
                        count['2B'] += 1
                    else:
                        count['2B'] = 1
                    count['B'] = 0
                else:
                    count[item] += 1
                print(count)
            else:
                count[item] = 1
        else:
            result = -1

    if result != -1:

        result = sum([price_table[item] * count[item] for item in count])

    return result






