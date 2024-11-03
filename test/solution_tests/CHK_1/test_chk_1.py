from solutions.CHK import checkout_solution


class TestR1Checkout:
    def test_empty(self):
        assert checkout_solution.checkout('') == 0

    def test_checkout(self):
        assert checkout_solution.checkout('A') == 50

    def test_checkout_2(self):
        assert checkout_solution.checkout('B') == 30

    def test_checkout_3(self):
        assert checkout_solution.checkout('CB') == 50

    def test_aa(self):
        assert checkout_solution.checkout('AA') == 100

    def test_discount_aaa(self):
        assert checkout_solution.checkout('AAA') == 130

    def test_discount_aaaa(self):
        assert checkout_solution.checkout('AAAA') == 180

    def test_discount_multiple_items(self):
        assert checkout_solution.checkout('BAAACADDB') == 275

    def test_invalid(self):
        assert checkout_solution.checkout('AxA') == -1


class TestR2Checkout:
    def test_ee(self):
        assert checkout_solution.checkout('EE') == 80

    def test_new_discount_5a(self):
        assert checkout_solution.checkout('AAAAA') == 200

    def test_new_discount_6a(self):
        assert checkout_solution.checkout('AAAAAA') == 250

    def test_new_discount_7a(self):
        assert checkout_solution.checkout('AAAAAAA') == 300

    def test_new_discount_8a(self):
        assert checkout_solution.checkout('AAAAAAAA') == 330

    def test_9a(self):
        assert checkout_solution.checkout('AAAAAAAAA') == 380

    def test_6a(self):
        assert checkout_solution.checkout('AAAAAA') == 250
        # {'3A': 0, '5A': 1,'A': 1}

    def test_eeeebb(self):
        assert checkout_solution.checkout('EEEEBB') == 160
        # {'3A': 0, '5A': 0, '2B': 0, 'B': 0, 'E': 4}

    def test_8e2b(self):
        assert checkout_solution.checkout('EEEEEEEEBB') == 320
        # {'3A': 0, '5A': 0, '2B': 0, 'B': 0, 'E': 8}

    def test_eeeb(self):
        assert checkout_solution.checkout('EEEB') == 120

    def test_2_of_each(self):
        assert checkout_solution.checkout('ABCDEABCDE') == 280

    def test_4e_2b(self):
        assert checkout_solution.checkout('EEEEBB') == 160

    def test_7e_5b(self):
        assert checkout_solution.checkout('EEEEEEEBBBBB') == 325


class TestR3Checkout:
    def test_1f(self):
        assert checkout_solution.checkout('F') == 10

    def test_2f(self):
        assert checkout_solution.checkout('FF') == 20

    def test_3f(self):
        assert checkout_solution.checkout('FFF') == 20

    def test_4f(self):
        assert checkout_solution.checkout('FFFF') == 30

    def test_5f(self):
        assert checkout_solution.checkout('FFFFF') == 40

    def test_6f(self):
        assert checkout_solution.checkout('FFFFFF') == 40

    def test_7f(self):
        assert checkout_solution.checkout('FFFFFFF') == 50

    def test_8f(self):
        assert checkout_solution.checkout('FFFFFFFF') == 60

    def test_9f(self):
        assert checkout_solution.checkout('FFFFFFFFF') == 60

    def test_10f(self):
        assert checkout_solution.checkout('FFFFFFFFFF') == 70

    def test_11f(self):
        assert checkout_solution.checkout('FFFFFFFFFFF') == 80

    def test_12f(self):
        assert checkout_solution.checkout('FFFFFFFFFFFF') == 80


class TestR4Checkout:
    # H
    def test_4h(self):
        assert checkout_solution.checkout('HHHH') == 40

    def test_5h(self):
        assert checkout_solution.checkout('HHHHH') == 45

    def test_9h(self):
        assert checkout_solution.checkout('HHHHHHHHH') == 85

    def test_10h(self):
        assert checkout_solution.checkout('HHHHHHHHHH') == 80

    def test_11h(self):
        assert checkout_solution.checkout('HHHHHHHHHHH') == 90

    def test_20h(self):
        assert checkout_solution.checkout('HHHHHHHHHHHHHHHHHHHH') == 160

    def test_21h(self):
        assert checkout_solution.checkout('HHHHHHHHHHHHHHHHHHHHH') == 170

    def test_25h(self):
        assert checkout_solution.checkout('HHHHHHHHHHHHHHHHHHHHHHHHH') == 205

    # K
    def test_1k(self):
        assert checkout_solution.checkout('K') == 80

    def test_2k(self):
        assert checkout_solution.checkout('KK') == 150

    def test_3k(self):
        assert checkout_solution.checkout('KKK') == 230

    def test_4k(self):
        assert checkout_solution.checkout('KKKK') == 300

    def test_5k(self):
        assert checkout_solution.checkout('KKKKK') == 380

    def test_10k(self):
        assert checkout_solution.checkout('KKKKKKKKKK') == 750

    def test_11k(self):
        assert checkout_solution.checkout('KKKKKKKKKKK') == 830

    # N
    def test_1n(self):
        assert checkout_solution.checkout('N') == 40

    def test_2n(self):
        assert checkout_solution.checkout('NN') == 80

    def test_3n(self):
        assert checkout_solution.checkout('NNN') == 120

    def test_4n1m(self):
        assert checkout_solution.checkout('NNNNM') == 160

    def test_8n2m(self):
        assert checkout_solution.checkout('NNNNNNNNMM') == 320

    def test_3n1m(self):
        assert checkout_solution.checkout('NNNM') == 120

    def test_2n2m(self):
        assert checkout_solution.checkout('NNMM') == 110

    def test_4n2m(self):
        assert checkout_solution.checkout('NNNNMM') == 175

    def test_7n5m(self):
        assert checkout_solution.checkout('NNNNNNNMMMMM') == 325

    # P
    def test_3p(self):
        assert checkout_solution.checkout('PPP') == 150

    def test_5p(self):
        assert checkout_solution.checkout('PPPPP') == 200

    def test_7p(self):
        assert checkout_solution.checkout('PPPPPPP') == 300

    def test_9p(self):
        assert checkout_solution.checkout('PPPPPPPPP') == 400

    def test_10p(self):
        assert checkout_solution.checkout('PPPPPPPPPP') == 400

    def test_11p(self):
        assert checkout_solution.checkout('PPPPPPPPPPP') == 450

    # Q
    def test_3q(self):
        assert checkout_solution.checkout('QQQ') == 80

    def test_5q(self):
        assert checkout_solution.checkout('QQQQQ') == 140

    def test_7q(self):
        assert checkout_solution.checkout('QQQQQQQ') == 190

    def test_9q(self):
        assert checkout_solution.checkout('QQQQQQQQQ') == 240

    def test_10q(self):
        assert checkout_solution.checkout('QQQQQQQQQQ') == 270

    def test_11q(self):
        assert checkout_solution.checkout('QQQQQQQQQQQ') == 300

    # R
    def test_1r(self):
        assert checkout_solution.checkout('R') == 50

    def test_2r(self):
        assert checkout_solution.checkout('RR') == 100

    def test_3r(self):
        assert checkout_solution.checkout('RRR') == 150

    def test_4r1q(self):
        assert checkout_solution.checkout('RRRRQ') == 200

    def test_8r2q(self):
        assert checkout_solution.checkout('RRRRRRRRQQ') == 400

    def test_3r1q(self):
        assert checkout_solution.checkout('RRRQ') == 150

    def test_2r2q(self):
        assert checkout_solution.checkout('RRQQ') == 160

    def test_4r2q(self):
        assert checkout_solution.checkout('RRRRQQ') == 230

    def test_7r6q(self):
        assert checkout_solution.checkout('RRRRRRRQQQQQQ') == 460 # (350+80+30)
        # 7R 6Q -> 350(7r) + 80 (3q) + 30 (1q)
    # U

    def test_1u(self):
        assert checkout_solution.checkout('U') == 40

    def test_2u(self):
        assert checkout_solution.checkout('UU') == 80

    def test_3u(self):
        assert checkout_solution.checkout('UUU') == 120

    def test_4u(self):
        assert checkout_solution.checkout('UUUU') == 120

    # def test_5u(self):
    #     assert checkout_solution.checkout('UUUUU') == 40
    #
    # def test_6u(self):
    #     assert checkout_solution.checkout('UUUUUU') == 40
    #
    # def test_7u(self):
    #     assert checkout_solution.checkout('UUUUUUU') == 50
    #
    # def test_8u(self):
    #     assert checkout_solution.checkout('UUUUUUUU') == 60
    #
    # def test_9u(self):
    #     assert checkout_solution.checkout('UUUUUUUUU') == 60
    #
    # def test_10u(self):
    #     assert checkout_solution.checkout('UUUUUUUUUU') == 70
    #
    # def test_11u(self):
    #     assert checkout_solution.checkout('UUUUUUUUUUU') == 80
    #
    # def test_12fu(self):
    #     assert checkout_solution.checkout('UUUUUUUUUUUU') == 80

    # V
    def test_v(self):
        assert checkout_solution.checkout('V') == 50

    def test_2v(self):
        assert checkout_solution.checkout('VV') == 90

    def test_3v(self):
        assert checkout_solution.checkout('VVV') == 130

    def test_4v(self):
        assert checkout_solution.checkout('VVVV') == 180

    def test_from_deploy(self):
        assert checkout_solution.checkout('PPPPQRUVPQRUVPQRUVSU') == 740
        # PPP PPP QQQ RRR S UUUU VVV