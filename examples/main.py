import olcarpc as rpc

with rpc.Client() as client:
    for actor in client.actors():
        print('Actor: %s' % actor.name)

    for category in client.categories():
        print('Category: %s' % category.name)

    for currency in client.currencies():
        print('Currency: %s' % currency.name)

    for dqs in client.dq_systems():
        print('DQSystem: %s' % dqs.name)

    for flow in client.flows():
        print('Flow: %s' % flow.name)

    for prop in client.flow_properties():
        print('FlowProperty: %s' % prop.name)

    for impact in client.impact_categories():
        print('ImpactCategory: %s' % impact.name)

    for method in client.impact_methods():
        print('ImpactMethod: %s' % method.name)

    for location in client.locations():
        print('Location: %s' % location.name)

    for parameter in client.parameters():
        print('Parameter: %s' % parameter.name)

    for process in client.processes():
        print('Process: %s' % process.name)

    for system in client.product_systems():
        print('ProductSystem: %s' % system.name)

    for project in client.projects():
        print('Project: %s' % project.name)

    for indicator in client.social_indicators():
        print('SocialIndicator: %s' % indicator.name)

    for source in client.sources():
        print('Source: %s' % source.name)

    for group in client.unit_groups():
        print('UnitGroup: %s' % group.name)