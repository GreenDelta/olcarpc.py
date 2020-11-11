import olcarpc as rpc
import unittest
import uuid


class LocationTest(unittest.TestCase):

    def setUp(self):
        self.client = rpc.Client()

    def tearDown(self):
        self.client.close()

    def test_non_existing(self):
        # check for ID
        status = self.client.location('non existing Location')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

        # check for name
        status = self.client.location(name='non existing Location')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

    def test_get_location(self):
        location = self.__location__()

        # check for ID
        status = self.client.location(location.id)
        self.assertTrue(status.ok)
        self.assertEqual(status.location.id, location.id)

        # check for name
        status = self.client.location(name=location.name)
        self.assertTrue(status.ok)
        self.assertEqual(status.location.name, location.name)

        self.assertTrue(self.client.delete(location).ok)

    def test_get_locations(self):
        locations = []
        for _i in range(0, 10):
            locations.append(self.__location__())
        location_ids = set()
        for location in self.client.locations():
            location_ids.add(location.id)
        for location in locations:
            self.assertTrue(location.id in location_ids)
            self.assertTrue(self.client.delete(location).ok)

    def test_location_atts(self):
        orig = self.__location__()
        clone: rpc.Location = self.client.location(orig.id).location

        self.assertEqual('Location', clone.type)
        self.assertEqual(orig.id, clone.id)
        self.assertEqual(orig.name, clone.name)
        self.assertEqual(orig.version, clone.version)
        self.assertEqual(orig.last_change, clone.last_change)

        # TODO: check specific fields

        self.assertTrue(self.client.delete(clone).ok)

    def __location__(self) -> rpc.Location:
        location = rpc.Location(
            id=str(uuid.uuid4()),
            name='Test Location',
            version='10.00.000',
        )
        status = self.client.put_location(location)
        self.assertTrue(status.ok)
        return location
