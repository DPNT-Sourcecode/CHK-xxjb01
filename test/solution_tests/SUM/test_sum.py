from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_negative_sum(self):
        assert sum_solution.compute(-2,-2) == -4

    def test_zero_sum(self):
        assert sum_solution.compute(0, 0) == 0
