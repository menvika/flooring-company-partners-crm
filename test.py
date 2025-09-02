import unittest


def discount_calculation(total):
    if total > 300000:
        return 15
    elif total > 50000:
        return 10
    elif total > 10000:
        return 5
    else:
        return 0



class test(unittest.TestCase):
    def test_sale(self):
        self.assertEqual(discount_calculation(0), 0)
        self.assertEqual(discount_calculation(10000), 0)
        self.assertEqual(discount_calculation(10001), 5)
        self.assertEqual(discount_calculation(50000), 5)
        self.assertEqual(discount_calculation(50001), 10)
        self.assertEqual(discount_calculation(300000), 10)
        self.assertEqual(discount_calculation(300001), 15)