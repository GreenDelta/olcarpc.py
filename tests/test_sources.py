import olcarpc as rpc
import unittest
import uuid


class SourceTest(unittest.TestCase):

    def setUp(self):
        self.client = rpc.Client()

    def tearDown(self):
        self.client.close()

    def test_non_existing(self):
        # check for ID
        status = self.client.get_source('non existing Source')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

        # check for name
        status = self.client.get_source(name='non existing Source')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

    def test_get_source(self):
        source = self.__source__()

        # check for ID
        status = self.client.get_source(source.id)
        self.assertTrue(status.ok)
        self.assertEqual(status.source.id, source.id)

        # check for name
        status = self.client.get_source(name=source.name)
        self.assertTrue(status.ok)
        self.assertEqual(status.source.name, source.name)

        self.assertTrue(self.client.delete(source).ok)

    def test_get_sources(self):
        sources = []
        for _i in range(0, 10):
            sources.append(self.__source__())
        source_ids = set()
        for source in self.client.get_sources():
            source_ids.add(source.id)
        for source in sources:
            self.assertTrue(source.id in source_ids)
            self.assertTrue(self.client.delete(source).ok)

    def test_source_atts(self):
        orig = self.__source__()
        clone: rpc.Source = self.client.get_source(orig.id).source

        self.assertEqual('Source', clone.type)
        self.assertEqual(orig.id, clone.id)
        self.assertEqual(orig.name, clone.name)
        self.assertEqual(orig.version, clone.version)
        self.assertEqual(orig.last_change, clone.last_change)

        # TODO: check specific fields

        self.assertTrue(self.client.delete(clone).ok)

    def __source__(self) -> rpc.Source:
        source = rpc.Source(
            id=str(uuid.uuid4()),
            name='Test Source',
            version='10.00.000',
        )
        status = self.client.put_source(source)
        self.assertTrue(status.ok)
        return source
