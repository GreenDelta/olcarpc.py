import olcarpc as rpc
import unittest
import uuid


class FlowTest(unittest.TestCase):

    def setUp(self):
        self.client = rpc.Client()

    def tearDown(self):
        self.client.close()

    def test_non_existing(self):
        # check for ID
        status = self.client.get_flow('non existing flow')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

        # check for name
        status = self.client.get_flow(name='non existing flow')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

    def test_get_flow(self):
        flow = self.__flow__()

        # check for ID
        status = self.client.get_flow(flow.id)
        self.assertTrue(status.ok)
        self.assertEqual(status.flow.id, flow.id)

        # check for name
        status = self.client.get_flow(name=flow.name)
        self.assertTrue(status.ok)
        self.assertEqual(status.flow.name, flow.name)

        self.assertTrue(self.client.delete(flow).ok)

    def test_get_flows(self):
        flows = []
        for _i in range(0, 10):
            flows.append(self.__flow__())
        flow_ids = set()
        for f in self.client.get_flows():
            flow_ids.add(f.id)
        for f in flows:
            self.assertTrue(f.id in flow_ids)
            self.assertTrue(self.client.delete(f).ok)

    def test_flow_atts(self):
        orig = self.__flow__()
        clone: rpc.Flow = self.client.get_flow(orig.id).flow

        self.assertEqual('Flow', clone.type)
        self.assertEqual(orig.id, clone.id)
        self.assertEqual(orig.name, clone.name)
        self.assertEqual(orig.version, clone.version)
        self.assertEqual(orig.last_change, clone.last_change)

        self.assertEqual(orig.flow_type, clone.flow_type)
        # TODO: check specific fields

        self.assertTrue(self.client.delete(clone).ok)

    def __flow__(self) -> rpc.Flow:
        flow = rpc.Flow(
            id=str(uuid.uuid4()),
            name='Test flow',
            version='10.00.000',
            flow_type=rpc.FlowType.ELEMENTARY_FLOW,
        )
        status = self.client.put_flow(flow)
        self.assertTrue(status.ok)
        return flow
