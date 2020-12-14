import olcarpc as rpc
import unittest
import uuid


class FlowPropertyTest(unittest.TestCase):

    def setUp(self):
        self.client = rpc.Client()

    def tearDown(self):
        self.client.close()

    def test_non_existing(self):
        # check for ID
        status = self.client.get_flow_property('non existing FlowProperty')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

        # check for name
        status = self.client.get_flow_property(name='non existing FlowProperty')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

    def test_get_flow_property(self):
        flow_property = self.__flow_property__()

        # check for ID
        status = self.client.get_flow_property(flow_property.id)
        self.assertTrue(status.ok)
        self.assertEqual(status.flow_property.id, flow_property.id)

        # check for name
        status = self.client.get_flow_property(name=flow_property.name)
        self.assertTrue(status.ok)
        self.assertEqual(status.flow_property.name, flow_property.name)

        self.assertTrue(self.client.delete(flow_property).ok)

    def test_get_flow_properties(self):
        flow_properties = []
        for _i in range(0, 10):
            flow_properties.append(self.__flow_property__())
        flow_property_ids = set()
        for flow_property in self.client.get_flow_properties():
            flow_property_ids.add(flow_property.id)
        for flow_property in flow_properties:
            self.assertTrue(flow_property.id in flow_property_ids)
            self.assertTrue(self.client.delete(flow_property).ok)

    def test_flow_property_atts(self):
        orig = self.__flow_property__()
        clone: rpc.FlowProperty = self.client.get_flow_property(orig.id)\
            .flow_property

        self.assertEqual('FlowProperty', clone.type)
        self.assertEqual(orig.id, clone.id)
        self.assertEqual(orig.name, clone.name)
        self.assertEqual(orig.version, clone.version)
        self.assertEqual(orig.last_change, clone.last_change)

        # TODO: check specific fields

        self.assertTrue(self.client.delete(clone).ok)

    def __flow_property__(self) -> rpc.FlowProperty:
        flow_property = rpc.FlowProperty(
            id=str(uuid.uuid4()),
            name='Test FlowProperty',
            version='10.00.000',
        )
        status = self.client.put_flow_property(flow_property)
        self.assertTrue(status.ok)
        return flow_property
