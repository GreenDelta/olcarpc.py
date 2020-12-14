import olcarpc as rpc
import unittest


class UnitGroupTest(unittest.TestCase):

    def setUp(self):
        self.client = rpc.Client()

    def tearDown(self):
        self.client.close()

    def test_non_existing(self):
        # check for ID
        status = self.client.get_unit_group('non existing UnitGroup')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

        # check for name
        status = self.client.get_unit_group(name='non existing UnitGroup')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

    def test_get_unit_group(self):
        unit_group = self.__unit_group__()

        # check for ID
        status = self.client.get_unit_group(unit_group.id)
        self.assertTrue(status.ok)
        self.assertEqual(status.unit_group.id, unit_group.id)

        # check for name
        status = self.client.get_unit_group(name=unit_group.name)
        self.assertTrue(status.ok)
        self.assertEqual(status.unit_group.name, unit_group.name)

        self.assertTrue(self.client.delete(unit_group).ok)

    def test_get_unit_groups(self):
        unit_groups = []
        for _i in range(0, 10):
            unit_groups.append(self.__unit_group__())
        unit_group_ids = set()
        for unit_group in self.client.get_unit_groups():
            unit_group_ids.add(unit_group.id)
        for unit_group in unit_groups:
            self.assertTrue(unit_group.id in unit_group_ids)
            self.assertTrue(self.client.delete(unit_group).ok)

    def test_unit_group_atts(self):
        orig = self.__unit_group__()
        clone: rpc.UnitGroup = self.client.get_unit_group(orig.id).unit_group

        self.assertEqual('UnitGroup', clone.type)
        self.assertEqual(orig.id, clone.id)
        self.assertEqual(orig.name, clone.name)
        self.assertEqual(orig.version, clone.version)
        # self.assertEqual(orig.last_change, clone.last_change)

        self.assertEqual(1, len(clone.units))
        self.assertEqual('kg', clone.units[0].name)
        self.assertEqual(1.0, clone.units[0].conversion_factor)
        self.assertTrue(clone.units[0].reference_unit)

        self.assertTrue(self.client.delete(clone).ok)

    def __unit_group__(self) -> rpc.UnitGroup:
        unit_group = rpc.unit_group_of(
            'Test units',
            rpc.unit_of('kg'))
        status = self.client.put_unit_group(unit_group)
        self.assertTrue(status.ok)
        return unit_group
