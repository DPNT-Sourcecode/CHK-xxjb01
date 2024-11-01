from solutions.CHK import checkout_solution

class TestCheckout():
    def test_empty(self):
        assert checkout_solution.checkout('') == 0

    def test_checkout(self):
        assert checkout_solution.checkout('A') == 50

    def test_checkout_2(self):
        assert checkout_solution.checkout('B') == 30

    def test_checkout_3(self):
        assert checkout_solution.checkout('CB') == 50

    def test_two_A(self):
        assert checkout_solution.checkout('AA') == 100

    def test_discount_item(self):
        assert checkout_solution.checkout('AAA') == 130

    def test_discount_items(self):
        assert checkout_solution.checkout('AAAA') == 180

    def test_discount_multiple_items(self):
        assert checkout_solution.checkout('BAAACADDB') == 275

    def test_invalid(self):
        assert checkout_solution.checkout('AxA') == -1

    def test_add_B_when_2E(self):
        assert checkout_solution.checkout('EE') == 80

    def test_new_discount_5A(self):
        assert checkout_solution.checkout('AAAAA') == 200

    def test_new_discount_multiple(self):
        assert checkout_solution.checkout('AAAAAAAA') == 360

    # def test_7_as(self):
    #     assert checkout_solution.checkout('AAAAAAA') == 300
    #
    # def test_8_as(self):
    #     assert checkout_solution.checkout('AAAAAAAA') == 330
    #
    # def test_6_as(self):
    #     assert checkout_solution.checkout('AAAAAA') == 250
    #     # {'3A': 0, '5A': 1,'A': 1}
    #
    # def test_multiple_es(self):
    #     assert checkout_solution.checkout('EEEEBB') == 160
    #     # {'3A': 0, '5A': 0, '2B': 0, 'B': 0, 'E': 4}
    #
    # def test_8_es(self):
    #     assert checkout_solution.checkout('EEEEEEEEBB') == 320
    #     # {'3A': 0, '5A': 0, '2B': 0, 'B': 0, 'E': 8}


