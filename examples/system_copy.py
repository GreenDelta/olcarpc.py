import olcarpc as rpc
import datetime
import uuid


def main():
    client = rpc.Client()
    print('start at: %s' % datetime.datetime.now())
    dataset: rpc.ProtoDataSet = client.fetch.Get(rpc.GetRequest(
            type=rpc.ProductSystem,
            id='75f2ef6c-7b2a-4850-8b68-38254d926cde'))
    print('fetched at: %s' % datetime.datetime.now())
    dataset.product_system.id = str(uuid.uuid4())
    dataset.product_system.name = "copied thing"
    client.update.Put(dataset)
    print('put at: %s' % datetime.datetime.now())
    client.close()


if __name__ == '__main__':
    main()
