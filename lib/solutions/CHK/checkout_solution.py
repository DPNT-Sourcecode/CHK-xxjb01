

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

    # skus.split(",")



    partial = [-1 if item not in price_table else price_table[item] for item in skus if item in price_table]

    if -1 in partial:
        result = -1
    else:
        result = sum(partial)

    return result




