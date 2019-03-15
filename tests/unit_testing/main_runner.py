# Mohammad's
# Paths need to be fixed because this does not work
import unittest
import sys

sys.path.insert(0, '../../chat-service')
import test_main

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_main))

# initialize a runner, pass it to the suite and run it
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
