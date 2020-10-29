import olcarpc as rpc
import unittest
import uuid


class DQSystemTest(unittest.TestCase):

    def setUp(self):
        self.client = rpc.Client()

    def tearDown(self):
        self.client.close()

    def test_non_existing(self):
        # check for ID
        status = self.client.dq_system('non existing DQSystem')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

        # check for name
        status = self.client.dq_system(name='non existing DQSystem')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

    def test_get_dq_system(self):
        dq_system = self.__dq_system__()

        # check for ID
        status = self.client.dq_system(dq_system.id)
        self.assertTrue(status.ok)
        self.assertEquals(status.dq_system.id, dq_system.id)

        # check for name
        status = self.client.dq_system(name=dq_system.name)
        self.assertTrue(status.ok)
        self.assertEquals(status.dq_system.name, dq_system.name)

        self.assertTrue(self.client.delete(dq_system).ok)

    def test_get_dq_systems(self):
        dq_systems = []
        for _i in range(0, 10):
            dq_systems.append(self.__dq_system__())
        dq_system_ids = set()
        for dq_system in self.client.dq_systems():
            dq_system_ids.add(dq_system.id)
        for dq_system in dq_systems:
            self.assertTrue(dq_system.id in dq_system_ids)
            self.assertTrue(self.client.delete(dq_system).ok)

    def test_dq_system_atts(self):
        orig = self.__dq_system__()
        clone: rpc.DQSystem = self.client.dq_system(orig.id).dq_system

        self.assertEqual('DQSystem', clone.type)
        self.assertEqual(orig.id, clone.id)
        self.assertEqual(orig.name, clone.name)
        self.assertEqual(orig.version, clone.version)
        self.assertEqual(orig.last_change, clone.last_change)

        # TODO: check specific fields

        self.assertTrue(self.client.delete(clone).ok)

    def __dq_system__(self) -> rpc.DQSystem:
        dq_system = rpc.DQSystem(
            id=str(uuid.uuid4()),
            name='Test DQSystem',
            version='10.00.000',
        )
        status = self.client.put_dq_system(dq_system)
        self.assertTrue(status.ok)
        return dq_system
