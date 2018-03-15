""" venv/bin/python probemanager/manage.py test core.tests.test_tasks --settings=probemanager.settings.dev """
from django.test import TestCase

from core.models import Probe
from core.tasks import upload_url_http, deploy_rules, reload_probe
from rules.models import Source


# from unittest import skip


class TasksRulesTest(TestCase):
    fixtures = ['init', 'crontab', 'test-rules-source', 'test-core-server', 'test-core-probe']

    @classmethod
    def setUpTestData(cls):
        pass

    def test_deploy_rules(self):
        with self.assertRaises(TypeError):
            deploy_rules(Probe.get_by_id(1).name)
        self.assertEqual(deploy_rules('bad'), {"message": "Error - probe is None - param id not set : " + 'bad'})
        # self.assertEqual(deploy_rules(None), {"message": "Error - probe is None - param id not set : " + 'None'})

    def test_reload_probe(self):
        with self.assertRaises(TypeError):
            reload_probe(Probe.get_by_id(1).name)
        self.assertEqual(reload_probe('bad'), {"message": "Error - probe is None - param id not set : " + 'bad'})
        # self.assertEqual(reload_probe(None), {"message": "Error - probe is None - param id not set : " + 'None'})

    def test_upload_url_http(self):
        upload_url_http(Source.get_by_id(1).uri)
        self.assertEqual(upload_url_http('bad'), {"message": "Error - source is None - param id not set : " + 'bad'})
        # self.assertEqual(upload_url_http(None), {"message": "Error - source is None - param id not set : " + 'None'})
