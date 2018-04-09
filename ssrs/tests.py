import unittest
from ssrs import service


class SsrsTests(unittest.TestCase):
    def test_get_reports(self):
        rd_ssrs = service.RdSsrs()
        rd_ssrs.execute_report()
