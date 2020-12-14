import olcarpc as rpc
import unittest
import uuid


class ActorTest(unittest.TestCase):

    def setUp(self):
        self.client = rpc.Client()

    def tearDown(self):
        self.client.close()

    def test_non_existing(self):
        # check for ID
        status = self.client.get_actor('non existing Actor')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

        # check for name
        status = self.client.get_actor(name='non existing Actor')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

    def test_get_actor(self):
        actor = self.__actor__()

        # check for ID
        status = self.client.get_actor(actor.id)
        self.assertTrue(status.ok)
        self.assertEqual(status.actor.id, actor.id)

        # check for name
        status = self.client.get_actor(name=actor.name)
        self.assertTrue(status.ok)
        self.assertEqual(status.actor.name, actor.name)

        self.assertTrue(self.client.delete(actor).ok)

    def test_get_actors(self):
        actors = []
        for _i in range(0, 10):
            actors.append(self.__actor__())
        actor_ids = set()
        for actor in self.client.get_actors():
            actor_ids.add(actor.id)
        for actor in actors:
            self.assertTrue(actor.id in actor_ids)
            self.assertTrue(self.client.delete(actor).ok)

    def test_actor_atts(self):
        orig = self.__actor__()
        clone: rpc.Actor = self.client.get_actor(orig.id).actor

        self.assertEqual('Actor', clone.type)
        self.assertEqual(orig.id, clone.id)
        self.assertEqual(orig.name, clone.name)
        self.assertEqual(orig.version, clone.version)
        self.assertEqual(orig.last_change, clone.last_change)

        # TODO: check specific fields

        self.assertTrue(self.client.delete(clone).ok)

    def __actor__(self) -> rpc.Actor:
        actor = rpc.Actor(
            id=str(uuid.uuid4()),
            name='Test Actor',
            version='10.00.000',
        )
        status = self.client.put_actor(actor)
        self.assertTrue(status.ok)
        return actor
