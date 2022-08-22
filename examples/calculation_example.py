import olcarpc as rpc

if __name__ == '__main__':
    with rpc.Client() as client:

        # create a calculation setup
        system = rpc.ProtoRef(id='7d1cbce0-b5b3-47ba-95b5-014ab3c7f569')
        method = rpc.ProtoRef(id='99b9d86b-ec6f-4610-ba9f-68ebfe5691dd')
        setup = rpc.ProtoCalculationSetup(
            product_system=system,
            impact_method=method)

        result = client.results.Calculate(setup)

        # query the inventory
        i = 0
        for r in client.results.GetTotalInventory(result):
            print(r)
            i += 1
            if i == 10:
                break

        # query the impact results
        for r in client.results.GetTotalImpacts(result):
            print(r)

        client.results.Dispose(result)
