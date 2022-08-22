import olcarpc as rpc

if __name__ == '__main__':

    with rpc.Client() as client:

        # Create a calculation setup with the ID of a product system
        # and LCIA method. The result is then related to the quantitative
        # reference amount of that system, if not specified otherwise
        system = rpc.ProtoRef(id='7d1cbce0-b5b3-47ba-95b5-014ab3c7f569')
        method = rpc.ProtoRef(id='99b9d86b-ec6f-4610-ba9f-68ebfe5691dd')
        setup = rpc.ProtoCalculationSetup(
            product_system=system,
            impact_method=method)

        # run the calculation
        result = client.results.Calculate(setup)

        # print the first 10 items of the inventory result
        i = 0
        for r in client.results.GetTotalInventory(result):
            print(r)
            i += 1
            if i == 10:
                break

        # print the LCIA result
        for r in client.results.GetTotalImpacts(result):
            print(r)

        # dispose the result after a calculation if it is not needed anymore,
        # otherwise it will stay in memory
        client.results.Dispose(result)
