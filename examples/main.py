import olcarpc as rpc


def main():
    with rpc.Client() as client:
        kg = rpc.unit_of('kg')
        units = rpc.unit_group_of('Units of mass', kg)
        client.put_unit_group(units)

        mass = rpc.flow_property_of('Mass', units)
        client.put_flow_property(mass)

        co2 = rpc.elementary_flow_of('CO2', mass)
        client.put_flow(co2)

        steel = rpc.product_flow_of('Steel', mass)
        client.put_flow(steel)

        process = rpc.process_of('Steel production')
        steel_output = rpc.output_of(process, steel, 1.0)
        steel_output.quantitative_reference = True
        process.exchanges.append(steel_output)

        co2_output = rpc.output_of(process, co2, 2.0)
        process.exchanges.append(co2_output)

        client.put_process(process)


if __name__ == '__main__':
    main()
