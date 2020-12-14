import olcarpc as rpc
import unittest
import uuid


class CurrencyTest(unittest.TestCase):

    def setUp(self):
        self.client = rpc.Client()

    def tearDown(self):
        self.client.close()

    def test_non_existing(self):
        # check for ID
        status = self.client.get_currency('non existing Currency')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

        # check for name
        status = self.client.get_currency(name='non existing Currency')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

    def test_get_currency(self):
        currency = self.__currency__()

        # check for ID
        status = self.client.get_currency(currency.id)
        self.assertTrue(status.ok)
        self.assertEqual(status.currency.id, currency.id)

        # check for name
        status = self.client.get_currency(name=currency.name)
        self.assertTrue(status.ok)
        self.assertEqual(status.currency.name, currency.name)

        self.assertTrue(self.client.delete(currency).ok)

    def test_get_currencies(self):
        currencies = []
        for _i in range(0, 10):
            currencies.append(self.__currency__())
        currency_ids = set()
        for currency in self.client.get_currencies():
            currency_ids.add(currency.id)
        for currency in currencies:
            self.assertTrue(currency.id in currency_ids)
            self.assertTrue(self.client.delete(currency).ok)

    def test_currency_atts(self):
        orig = self.__currency__()
        clone: rpc.Currency = self.client.get_currency(orig.id).currency

        self.assertEqual('Currency', clone.type)
        self.assertEqual(orig.id, clone.id)
        self.assertEqual(orig.name, clone.name)
        self.assertEqual(orig.version, clone.version)
        self.assertEqual(orig.last_change, clone.last_change)

        # TODO: check specific fields

        self.assertTrue(self.client.delete(clone).ok)

    def __currency__(self) -> rpc.Currency:
        currency = rpc.Currency(
            id=str(uuid.uuid4()),
            name='Test Currency',
            version='10.00.000',
        )
        status = self.client.put_currency(currency)
        self.assertTrue(status.ok)
        return currency
