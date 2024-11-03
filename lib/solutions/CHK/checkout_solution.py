# noinspection PyUnusedLocal
# skus = unicode string
from tabnanny import check

price_table = {'A': 50, '3A': 130, '5A': 200, 'B': 30, '2B': 45, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20,
               'H': 10, '5H': 45, '10H': 80, 'I': 35, 'J': 60, 'K': 70, '2K':150, 'L': 90, 'M': 15,
               'N': 40, 'O': 10, 'P': 50, '5P':200, 'Q': 30, '3Q':80, 'R': 50, 'S': 20, 'T': 20,'U': 40,
               'V': 50, '2V':90, '3V':130, 'W': 20, 'X': 17, 'Y': 20, 'Z': 21}

def checkout(skus:str) -> int:

    result = 0
    discount = 0
    count = {'A': 0, '3A': 0, '5A': 0, 'B': 0, '2B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0,
               'H': 0, '5H': 0, '10H': 0, 'I': 0, 'J': 0, 'K': 0, '2K':0, 'L': 0, 'M': 0,
               'N': 0, 'O': 0, 'P': 0, '5P':0, 'Q': 0, '3Q': 0, 'R': 0, 'S': 0, 'T': 0,'U': 0,
               'V': 0, '2V':0, '3V':0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

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
        if count['B'] > 1:
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
            while counter >= 3:
                counter -= 3
                discount -= 10

    def clear_h():
        value = count['H']
        if value > 4:
            counter = value
            if count['H'] > 9:
                while counter >= 0:
                    count['10H'] += 1
                    counter -= 10
                    count['H'] -= 10
                    if counter <= 1 or count['H'] < 10:
                        break
            if count['H'] > 4:
                while counter >= 0:
                    count['5H'] += 1
                    counter -= 5
                    count['H'] -= 5
                    if counter <= 1 or count['H'] < 5:
                        break
    def clear_k():
        if count['K'] > 0:
            value = count['K']
            count['2K'] = int(value / 2)
            count['K'] = value % 2

    def clear_n():
        nonlocal discount
        value = count['N']
        counter = value
        if value >= 3:
            while counter >= 3:
                counter -= 3
                discount -= 15
                total_m = count['M']
                if total_m == 0:
                    count['M'] += 1

    def clear_p():
        if count['P'] > 4:
            value = count['P']
            count['5P'] = int(value / 5)
            count['P'] = value % 5

    def clear_q():
        if count['Q'] > 2:
            value = count['Q']
            count['3Q'] = int(value / 3)
            count['Q'] = value % 3

    def clear_r():
        nonlocal discount
        value = count['R']
        counter = value
        if value >= 3:
            while counter >= 3:
                counter -= 3
                if count['Q'] > 0:
                    count['Q'] -= 1

    def clear_u():
        nonlocal discount
        value = count['U']
        if value == 3:
            count['U'] += 1
            discount -= 40
        if value > 3:
            counter = count['U']
            while counter >= 4:
                counter -= 4
                discount -= 40

    def clear_v():
        value = count['V']
        if value >= 3:
            count['3V'] = int(value / 3)
            count['V'] = value - count['3V'] * 3

            if value % 3 >= 2:
                count['2V'] = int(value / 3)
                count['V'] = count['V'] - 2

        elif value < 3 and (value % 2 == 0 or (value - 1) % 2 == 0):
            count['2V'] = int(value / 2)
            count['V'] = value % 2


    def multi_discount():
        all_items_in_discount = ['S','T','X','Y','Z']
        discounting_from = {}

        for key, value in count.items():
            if key in all_items_in_discount and value > 0:
                discounting_from[key] = value

        total_items = sum([count[dis_item] for dis_item in all_items_in_discount])

        if total_items > 2:
            nonlocal discount
            print(discount, int(total_items/3))
            discount += 45 * int(total_items / 3)
            print(discount, int(total_items / 3))
            for k, v in discounting_from.items():
                print('k,v: ', k, v)
                print(f'output v%3: {k} -> {v % 3}')

                if v < 4:
                    count[k] = count[k] - v
                else:
                    count[k] = count[k] - (v % 3)


            # counter = total_items
            # while counter >= 3:
            #     if count['X'] > 0:
            #         count['X'] -= 1
            #     elif count['Y'] > 0:
            #         count['Y'] -= 1
            #     elif count['S'] > 0:
            #         count['S'] -= 1
            #     elif count['T'] > 0:
            #         count['T'] -= 1
            #     elif count['Z'] > 0:
            #         count['Z'] -= 1
            #
            #     counter -= 1

        # count['3Q'] = int(value / 3)
        # count['Q'] = value % 3


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
        clear_h()
        clear_k()
        clear_n()
        clear_p()
        clear_r()
        clear_q()
        clear_u()
        clear_v()
        multi_discount()

        result = sum([price_table[item] * count[item] for item in count]) + discount

    print(f'RESULT: {result}')
    print(f'COUNT: {count}')

    return result





