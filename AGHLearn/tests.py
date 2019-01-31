import unittest


def run_all_tests():
    suite = unittest.TestLoader().discover('Models/tests/', pattern="test_*.py")
    all_tests = unittest.TestSuite(suite)
    unittest.TextTestRunner(verbosity=5).run(all_tests)


if __name__ == "__main__":
    run_all_tests()