import olcarpc as rpc

if __name__ == '__main__':
    with rpc.Client() as client:
        system: rpc.Ref = client.get_descriptor(
            rpc.ProductSystem, name='compost plant, open').ref
        method: rpc.Ref = client.get_descriptor(
            rpc.ImpactMethod, name='TRACI [v2.1, February 2014]').ref
        result = client.calculate(system, method).result
        print(client.dispose(result))
