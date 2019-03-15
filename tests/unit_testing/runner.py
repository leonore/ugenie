# testsrunner.py
import unittest
import sys
#elastic path
#path should be changed
sys.path.insert(0, '/home/ubuntu/dissertation/tests/unit_testing')
# import your test modules
import test_elastic



# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite
###suite.addTests(loader.loadTestsFromModule(soketio_test))
suite.addTests(loader.loadTestsFromModule(test_elastic))


# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)