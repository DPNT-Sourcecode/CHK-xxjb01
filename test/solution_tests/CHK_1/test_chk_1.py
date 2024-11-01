from solutions.CHK import checkout_solution

class TestCheckout():
    def test_empty(self):
        assert checkout_solution.checkout('') == 0

    def test_checkout(self):
        assert checkout_solution.checkout('A') == 50
        assert checkout_solution.checkout('B') == 30
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

    def test_new_discount(self):
        assert checkout_solution.checkout('AAAAA') == 200

    def test_new_discount_multiple(self):
        assert checkout_solution.checkout('AAAAAAAA') == 430
