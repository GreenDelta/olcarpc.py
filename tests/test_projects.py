import olcarpc as rpc
import unittest
import uuid


class ProjectTest(unittest.TestCase):

    def setUp(self):
        self.client = rpc.Client()

    def tearDown(self):
        self.client.close()

    def test_non_existing(self):
        # check for ID
        status = self.client.project('non existing Project')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

        # check for name
        status = self.client.project(name='non existing Project')
        self.assertFalse(status.ok)
        self.assertTrue(len(status.error) > 0)

    def test_get_project(self):
        project = self.__project__()

        # check for ID
        status = self.client.project(project.id)
        self.assertTrue(status.ok)
        self.assertEquals(status.project.id, project.id)

        # check for name
        status = self.client.project(name=project.name)
        self.assertTrue(status.ok)
        self.assertEquals(status.project.name, project.name)

        self.assertTrue(self.client.delete(project).ok)

    def test_get_projects(self):
        projects = []
        for _i in range(0, 10):
            projects.append(self.__project__())
        project_ids = set()
        for project in self.client.projects():
            project_ids.add(project.id)
        for project in projects:
            self.assertTrue(project.id in project_ids)
            self.assertTrue(self.client.delete(project).ok)

    def test_project_atts(self):
        orig = self.__project__()
        clone: rpc.Project = self.client.project(orig.id).project

        self.assertEqual('Project', clone.type)
        self.assertEqual(orig.id, clone.id)
        self.assertEqual(orig.name, clone.name)
        self.assertEqual(orig.version, clone.version)
        self.assertEqual(orig.last_change, clone.last_change)

        # TODO: check specific fields

        self.assertTrue(self.client.delete(clone).ok)

    def __project__(self) -> rpc.Project:
        project = rpc.Project(
            id=str(uuid.uuid4()),
            name='Test Project',
            version='10.00.000',
        )
        status = self.client.put_project(project)
        self.assertTrue(status.ok)
        return project
