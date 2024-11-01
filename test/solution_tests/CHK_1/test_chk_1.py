from solutions.CHK import checkout_solution

price_table = {'3A': 130,'2B': 45, 'A': 50, 'B': 30, 'C': 20, 'D': 15 }

class TestCheckout():
    def test_empty(self):
        assert checkout_solution.checkout('') == 0

    def test_checkout(self):
        assert checkout_solution.checkout('A') == 50
        assert checkout_solution.checkout('B') == 30
        assert checkout_solution.checkout('CB') == 50

    def test_discount_item(self):
        assert checkout_solution.checkout('AAA') == 130

    def test_discount_items(self):
        assert checkout_solution.checkout('AAAA') == 180

    def test_discount_multiple_items(self):
        assert checkout_solution.checkout('BAAACADDB') == 275

    def test_invalid(self):
        assert checkout_solution.checkout('AxA') == -1






