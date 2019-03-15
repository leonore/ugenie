import unittest
import sys

sys.path.append('../../chat-service/model')
sys.path.append('../../chat-service/')
import test_elastic
import test_main
# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test_elastic))
suite.addTests(loader.loadTestsFromModule(test_main))
# initialize a runner, pass it to the suite and run it
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
