import olcarpc as rpc
import unittest
import uuid


class FlowTest(unittest.TestCase):

    def setUp(self):
        self.client = rpc.Client()
        self.flow = rpc.Flow(
            id=str(uuid.uuid4()),
            name='Test flow',
            flow_type=rpc.FlowType.ELEMENTARY_FLOW)
        self.client.put_flow(self.flow)

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

    def test_get_flow(self):
        # check for ID
        status = self.client.flow(self.flow.id)
        self.assertTrue(status.ok)
        self.assertEquals(status.flow.id, self.flow.id)

        # check for name
        status = self.client.flow(name=self.flow.name)
        self.assertTrue(status)
        self.assertEquals(status.flow.name, self.flow.name)