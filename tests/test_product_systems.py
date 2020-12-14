import olcarpc as rpc
import unittest
import uuid


class ProductSystemTest(unittest.TestCase):

    def setUp(self):
        self.client = rpc.Client()

    def tearDown(self):
        self.client.close()

    def test_non_existing(self):
        # check for ID
        status = self.client.get_product_system('non existing ProductSystem')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

        # check for name
        status = self.client.get_product_system(
            name='non existing ProductSystem')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

    def test_get_product_system(self):
        product_system = self.__product_system__()

        # check for ID
        status = self.client.get_product_system(product_system.id)
        self.assertTrue(status.ok)
        self.assertEqual(status.product_system.id, product_system.id)

        # check for name
        status = self.client.get_product_system(name=product_system.name)
        self.assertTrue(status.ok)
        self.assertEqual(status.product_system.name, product_system.name)

        self.assertTrue(self.client.delete(product_system).ok)

    def test_get_product_systems(self):
        product_systems = []
        for _i in range(0, 10):
            product_systems.append(self.__product_system__())
        product_system_ids = set()
        for product_system in self.client.get_product_systems():
            product_system_ids.add(product_system.id)
        for product_system in product_systems:
            self.assertTrue(product_system.id in product_system_ids)
            self.assertTrue(self.client.delete(product_system).ok)

    def test_product_system_atts(self):
        orig = self.__product_system__()
        clone: rpc.ProductSystem = self.client.get_product_system(orig.id)\
            .product_system

        self.assertEqual('ProductSystem', clone.type)
        self.assertEqual(orig.id, clone.id)
        self.assertEqual(orig.name, clone.name)
        self.assertEqual(orig.version, clone.version)
        self.assertEqual(orig.last_change, clone.last_change)

        # TODO: check specific fields

        self.assertTrue(self.client.delete(clone).ok)

    def __product_system__(self) -> rpc.ProductSystem:
        product_system = rpc.ProductSystem(
            id=str(uuid.uuid4()),
            name='Test ProductSystem',
            version='10.00.000',
        )
        status = self.client.put_product_system(product_system)
        self.assertTrue(status.ok)
        return product_system
