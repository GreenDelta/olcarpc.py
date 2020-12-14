import olcarpc as rpc
import unittest
import uuid


class ProcessTest(unittest.TestCase):

    def setUp(self):
        self.client = rpc.Client()

    def tearDown(self):
        self.client.close()

    def test_non_existing(self):
        # check for ID
        status = self.client.get_process('non existing Process')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

        # check for name
        status = self.client.get_process(name='non existing Process')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

    def test_get_process(self):
        process = self.__process__()

        # check for ID
        status = self.client.get_process(process.id)
        self.assertTrue(status.ok)
        self.assertEqual(status.process.id, process.id)

        # check for name
        status = self.client.get_process(name=process.name)
        self.assertTrue(status.ok)
        self.assertEqual(status.process.name, process.name)

        self.assertTrue(self.client.delete(process).ok)

    def test_get_processes(self):
        processes = []
        for _i in range(0, 10):
            processes.append(self.__process__())
        process_ids = set()
        for process in self.client.get_processes():
            process_ids.add(process.id)
        for process in processes:
            self.assertTrue(process.id in process_ids)
            self.assertTrue(self.client.delete(process).ok)

    def test_process_atts(self):
        orig = self.__process__()
        clone: rpc.Process = self.client.get_process(orig.id).process

        self.assertEqual('Process', clone.type)
        self.assertEqual(orig.id, clone.id)
        self.assertEqual(orig.name, clone.name)
        self.assertEqual(orig.version, clone.version)
        self.assertEqual(orig.last_change, clone.last_change)

        # TODO: check specific fields

        self.assertTrue(self.client.delete(clone).ok)

    def __process__(self) -> rpc.Process:
        process = rpc.Process(
            id=str(uuid.uuid4()),
            name='Test Process',
            version='10.00.000',
        )
        status = self.client.put_process(process)
        self.assertTrue(status.ok)
        return process
