from solutions.CHK import checkout_solution

class TestR1Checkout():
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

class TestR2Checkout():
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






