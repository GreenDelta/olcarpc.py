import olcarpc as rpc
import unittest
import uuid


class SocialIndicatorTest(unittest.TestCase):

    def setUp(self):
        self.client = rpc.Client()

    def tearDown(self):
        self.client.close()

    def test_non_existing(self):
        # check for ID
        status = self.client.social_indicator('non existing SocialIndicator')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

        # check for name
        status = self.client.social_indicator(name='non existing SocialIndicator')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

    def test_get_social_indicator(self):
        social_indicator = self.__social_indicator__()

        # check for ID
        status = self.client.social_indicator(social_indicator.id)
        self.assertTrue(status.ok)
        self.assertEqual(status.social_indicator.id, social_indicator.id)

        # check for name
        status = self.client.social_indicator(name=social_indicator.name)
        self.assertTrue(status.ok)
        self.assertEqual(status.social_indicator.name, social_indicator.name)

        self.assertTrue(self.client.delete(social_indicator).ok)

    def test_get_social_indicators(self):
        social_indicators = []
        for _i in range(0, 10):
            social_indicators.append(self.__social_indicator__())
        social_indicator_ids = set()
        for social_indicator in self.client.social_indicators():
            social_indicator_ids.add(social_indicator.id)
        for social_indicator in social_indicators:
            self.assertTrue(social_indicator.id in social_indicator_ids)
            self.assertTrue(self.client.delete(social_indicator).ok)

    def test_social_indicator_atts(self):
        orig = self.__social_indicator__()
        clone: rpc.SocialIndicator = self.client.social_indicator(orig.id).social_indicator

        self.assertEqual('SocialIndicator', clone.type)
        self.assertEqual(orig.id, clone.id)
        self.assertEqual(orig.name, clone.name)
        self.assertEqual(orig.version, clone.version)
        self.assertEqual(orig.last_change, clone.last_change)

        # TODO: check specific fields

        self.assertTrue(self.client.delete(clone).ok)

    def __social_indicator__(self) -> rpc.SocialIndicator:
        social_indicator = rpc.SocialIndicator(
            id=str(uuid.uuid4()),
            name='Test SocialIndicator',
            version='10.00.000',
        )
        status = self.client.put_social_indicator(social_indicator)
        self.assertTrue(status.ok)
        return social_indicator
