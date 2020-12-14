import olcarpc as rpc
import unittest
import uuid


class ParameterTest(unittest.TestCase):

    def setUp(self):
        self.client = rpc.Client()

    def tearDown(self):
        self.client.close()

    def test_non_existing(self):
        # check for ID
        status = self.client.get_parameter('non existing Parameter')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

        # check for name
        status = self.client.get_parameter(name='non existing Parameter')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

    def test_get_parameter(self):
        parameter = self.__parameter__()

        # check for ID
        status = self.client.get_parameter(parameter.id)
        self.assertTrue(status.ok)
        self.assertEqual(status.parameter.id, parameter.id)

        # check for name
        status = self.client.get_parameter(name=parameter.name)
        self.assertTrue(status.ok)
        self.assertEqual(status.parameter.name, parameter.name)

        self.assertTrue(self.client.delete(parameter).ok)

    def test_get_parameters(self):
        parameters = []
        for _i in range(0, 10):
            parameters.append(self.__parameter__())
        parameter_ids = set()
        for parameter in self.client.get_parameters():
            parameter_ids.add(parameter.id)
        for parameter in parameters:
            self.assertTrue(parameter.id in parameter_ids)
            self.assertTrue(self.client.delete(parameter).ok)

    def test_parameter_atts(self):
        orig = self.__parameter__()
        clone: rpc.Parameter = self.client.get_parameter(orig.id).parameter

        self.assertEqual('Parameter', clone.type)
        self.assertEqual(orig.id, clone.id)
        self.assertEqual(orig.name, clone.name)
        self.assertEqual(orig.version, clone.version)
        self.assertEqual(orig.last_change, clone.last_change)

        # TODO: check specific fields

        self.assertTrue(self.client.delete(clone).ok)

    def __parameter__(self) -> rpc.Parameter:
        parameter = rpc.Parameter(
            id=str(uuid.uuid4()),
            name='Test Parameter',
            version='10.00.000',
        )
        status = self.client.put_parameter(parameter)
        self.assertTrue(status.ok)
        return parameter
