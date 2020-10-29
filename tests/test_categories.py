import olcarpc as rpc
import unittest
import uuid


class CategoryTest(unittest.TestCase):

    def setUp(self):
        self.client = rpc.Client()

    def tearDown(self):
        self.client.close()

    def test_non_existing(self):
        # check for ID
        status = self.client.category('non existing Category')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

        # check for name
        status = self.client.category(name='non existing Category')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

    def test_get_category(self):
        category = self.__category__()

        # check for ID
        status = self.client.category(category.id)
        self.assertTrue(status.ok)
        self.assertEquals(status.category.id, category.id)

        # check for name
        status = self.client.category(name=category.name)
        self.assertTrue(status.ok)
        self.assertEquals(status.category.name, category.name)

        self.assertTrue(self.client.delete(category).ok)

    def test_get_categories(self):
        categories = []
        for _i in range(0, 10):
            categories.append(self.__category__())
        category_ids = set()
        for category in self.client.categories():
            category_ids.add(category.id)
        for category in categories:
            self.assertTrue(category.id in category_ids)
            self.assertTrue(self.client.delete(category).ok)

    def test_category_atts(self):
        orig = self.__category__()
        clone: rpc.Category = self.client.category(orig.id).category

        self.assertEqual('Category', clone.type)
        self.assertEqual(orig.id, clone.id)
        self.assertEqual(orig.name, clone.name)
        self.assertEqual(orig.version, clone.version)
        self.assertEqual(orig.last_change, clone.last_change)

        # TODO: check specific fields

        self.assertTrue(self.client.delete(clone).ok)

    def __category__(self) -> rpc.Category:
        category = rpc.Category(
            id=str(uuid.uuid4()),
            name='Test Category',
            version='10.00.000',
        )
        status = self.client.put_category(category)
        self.assertTrue(status.ok)
        return category
