import olcarpc as rpc
import unittest


class ProviderTest(unittest.TestCase):

    def setUp(self) -> None:
        self.client = rpc.Client()

    def tearDown(self) -> None:
        self.client.close()

    def test_no_providers(self):
        providers = self.client.get_providers_of(
            rpc.FlowRef(name="does not exist"))
        i = 0
        for _ in providers:
            i += 1
        self.assertEqual(0, i)

    def test_find_provider(self):

        # create the model
        kg = rpc.unit_of('kg')
        units = rpc.unit_group_of('Mass units', kg)
        mass = rpc.flow_property_of('Mass', units)
        steel = rpc.product_flow_of('Steel', mass)
        process = rpc.process_of('Steel production')
        output = rpc.output_of(process, steel, 1.0)
        process.exchanges.append(output)

        # insert the model
        self.client.put_unit_group(units)
        self.client.put_flow_property(mass)
        self.client.put_flow(steel)
        self.client.put_process(process)

        # check that we can find the process
        # as provider
        provider = next(self.client.get_providers_of(steel))
        self.assertEqual(process.id, provider.id)

        # delete the model
        self.client.delete(process)
        self.client.delete(steel)
        self.client.delete(mass)
        self.client.delete(units)


