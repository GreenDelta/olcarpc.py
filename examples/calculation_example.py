import olcarpc as rpc

if __name__ == '__main__':
    with rpc.Client() as client:

        # select the product system and LCIA method and calculate the result
        system: rpc.Ref = client.get_descriptor(
            rpc.ProductSystem, name='compost plant, open').ref
        method: rpc.Ref = client.get_descriptor(
            rpc.ImpactMethod, name='TRACI [v2.1, February 2014]').ref
        result = client.calculate(system, method).result

        # query the inventory
        i = 0
        for r in client.get_inventory(result):
            print(r)
            i += 1
            if i == 10:
                break

        # query the impact results
        for r in client.get_impacts(result):
            print(r)

        print(client.dispose(result))
