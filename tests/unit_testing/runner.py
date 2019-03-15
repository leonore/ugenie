import unittest
import sys

sys.path.append('../../chat-service/model')
import test_elastic

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test_elastic))

# initialize a runner, pass it to the suite and run it
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
