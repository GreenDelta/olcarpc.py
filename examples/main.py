import olcarpc

with olcarpc.Client() as client:
    for a in client.actors:
        print(a.name)
