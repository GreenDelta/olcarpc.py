import olcarpc as rpc
import unittest


class FlowTest(unittest.TestCase):

    def setUp(self):
        self.client = rpc.Client()

    def tearDown(self):
        self.client.close()

    def test_not_exists(self):
        # check for ID
        status = self.client.flow('non existing flow')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

        # check for name
        status = self.client.flow(name='non existing flow')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)
