import olcarpc as rpc
import unittest
import uuid


class ImpactMethodTest(unittest.TestCase):

    def setUp(self):
        self.client = rpc.Client()

    def tearDown(self):
        self.client.close()

    def test_non_existing(self):
        # check for ID
        status = self.client.get_impact_method('non existing ImpactMethod')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

        # check for name
        status = self.client.get_impact_method(name='non existing ImpactMethod')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

    def test_get_impact_method(self):
        impact_method = self.__impact_method__()

        # check for ID
        status = self.client.get_impact_method(impact_method.id)
        self.assertTrue(status.ok)
        self.assertEqual(status.impact_method.id, impact_method.id)

        # check for name
        status = self.client.get_impact_method(name=impact_method.name)
        self.assertTrue(status.ok)
        self.assertEqual(status.impact_method.name, impact_method.name)

        self.assertTrue(self.client.delete(impact_method).ok)

    def test_get_impact_methods(self):
        impact_methods = []
        for _i in range(0, 10):
            impact_methods.append(self.__impact_method__())
        impact_method_ids = set()
        for impact_method in self.client.get_impact_methods():
            impact_method_ids.add(impact_method.id)
        for impact_method in impact_methods:
            self.assertTrue(impact_method.id in impact_method_ids)
            self.assertTrue(self.client.delete(impact_method).ok)

    def test_impact_method_atts(self):
        orig = self.__impact_method__()
        clone: rpc.ImpactMethod = self.client.get_impact_method(orig.id)\
            .impact_method

        self.assertEqual('ImpactMethod', clone.type)
        self.assertEqual(orig.id, clone.id)
        self.assertEqual(orig.name, clone.name)
        self.assertEqual(orig.version, clone.version)
        self.assertEqual(orig.last_change, clone.last_change)

        # TODO: check specific fields

        self.assertTrue(self.client.delete(clone).ok)

    def __impact_method__(self) -> rpc.ImpactMethod:
        impact_method = rpc.ImpactMethod(
            id=str(uuid.uuid4()),
            name='Test ImpactMethod',
            version='10.00.000',
        )
        status = self.client.put_impact_method(impact_method)
        self.assertTrue(status.ok)
        return impact_method
