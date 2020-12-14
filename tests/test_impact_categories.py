import olcarpc as rpc
import unittest
import uuid


class ImpactCategoryTest(unittest.TestCase):

    def setUp(self):
        self.client = rpc.Client()

    def tearDown(self):
        self.client.close()

    def test_non_existing(self):
        # check for ID
        status = self.client.get_impact_category('non existing ImpactCategory')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

        # check for name
        status = self.client.get_impact_category(
            name='non existing ImpactCategory')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

    def test_get_impact_category(self):
        impact_category = self.__impact_category__()

        # check for ID
        status = self.client.get_impact_category(impact_category.id)
        self.assertTrue(status.ok)
        self.assertEqual(status.impact_category.id, impact_category.id)

        # check for name
        status = self.client.get_impact_category(name=impact_category.name)
        self.assertTrue(status.ok)
        self.assertEqual(status.impact_category.name, impact_category.name)

        self.assertTrue(self.client.delete(impact_category).ok)

    def test_get_impact_categories(self):
        impact_categories = []
        for _i in range(0, 10):
            impact_categories.append(self.__impact_category__())
        impact_category_ids = set()
        for impact_category in self.client.get_impact_categories():
            impact_category_ids.add(impact_category.id)
        for impact_category in impact_categories:
            self.assertTrue(impact_category.id in impact_category_ids)
            self.assertTrue(self.client.delete(impact_category).ok)

    def test_impact_category_atts(self):
        orig = self.__impact_category__()
        clone: rpc.ImpactCategory = self.client.get_impact_category(orig.id)\
            .impact_category

        self.assertEqual('ImpactCategory', clone.type)
        self.assertEqual(orig.id, clone.id)
        self.assertEqual(orig.name, clone.name)
        self.assertEqual(orig.version, clone.version)
        self.assertEqual(orig.last_change, clone.last_change)

        # TODO: check specific fields

        self.assertTrue(self.client.delete(clone).ok)

    def __impact_category__(self) -> rpc.ImpactCategory:
        impact_category = rpc.ImpactCategory(
            id=str(uuid.uuid4()),
            name='Test ImpactCategory',
            version='10.00.000',
        )
        status = self.client.put_impact_category(impact_category)
        self.assertTrue(status.ok)
        return impact_category
