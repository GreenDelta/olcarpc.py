import olcarpc as rpc
import datetime
import uuid


if __name__ == '__main__':
    client = rpc.Client()
    print('start at: %s' % datetime.datetime.now())
    sys: rpc.ProductSystem = client.get_product_system(
        '4d4eb50c-3943-41c0-a90a-34b621474271').product_system
    print('fetched at: %s' % datetime.datetime.now())
    sys.id = str(uuid.uuid4())
    sys.name = "copied thing"
    client.put_product_system(sys)
    print('put at: %s' % datetime.datetime.now())
    print(sys.name)
    client.close()
