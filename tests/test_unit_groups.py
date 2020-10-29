import olcarpc as rpc
import unittest
import uuid


class UnitGroupTest(unittest.TestCase):

    def setUp(self):
        self.client = rpc.Client()

    def tearDown(self):
        self.client.close()

    def test_non_existing(self):
        # check for ID
        status = self.client.unit_group('non existing UnitGroup')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

        # check for name
        status = self.client.unit_group(name='non existing UnitGroup')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

    def test_get_unit_group(self):
        unit_group = self.__unit_group__()

        # check for ID
        status = self.client.unit_group(unit_group.id)
        self.assertTrue(status.ok)
        self.assertEquals(status.unit_group.id, unit_group.id)

        # check for name
        status = self.client.unit_group(name=unit_group.name)
        self.assertTrue(status.ok)
        self.assertEquals(status.unit_group.name, unit_group.name)

        self.assertTrue(self.client.delete(unit_group).ok)

    def test_get_unit_groups(self):
        unit_groups = []
        for _i in range(0, 10):
            unit_groups.append(self.__unit_group__())
        unit_group_ids = set()
        for unit_group in self.client.unit_groups():
            unit_group_ids.add(unit_group.id)
        for unit_group in unit_groups:
            self.assertTrue(unit_group.id in unit_group_ids)
            self.assertTrue(self.client.delete(unit_group).ok)

    def test_unit_group_atts(self):
        orig = self.__unit_group__()
        clone: rpc.UnitGroup = self.client.unit_group(orig.id).unit_group

        self.assertEqual('UnitGroup', clone.type)
        self.assertEqual(orig.id, clone.id)
        self.assertEqual(orig.name, clone.name)
        self.assertEqual(orig.version, clone.version)
        self.assertEqual(orig.last_change, clone.last_change)

        # TODO: check specific fields

        self.assertTrue(self.client.delete(clone).ok)

    def __unit_group__(self) -> rpc.UnitGroup:
        unit_group = rpc.UnitGroup(
            id=str(uuid.uuid4()),
            name='Test UnitGroup',
            version='10.00.000',
        )
        status = self.client.put_unit_group(unit_group)
        self.assertTrue(status.ok)
        return unit_group
