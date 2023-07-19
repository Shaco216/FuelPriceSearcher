import unittest

from DBServiceManagement_Windows import DBServiceManagement


class test_DBServiceManagement_Windows(unittest.TestCase):
    def test_service_check(self):
        expected = "running"
        service = "MySQL80"
        DBService = DBServiceManagement()
        DBService.start_service(service)
        self.assertEqual(DBService.check_service_is_running(service),expected)
        DBService.stop_service(service)