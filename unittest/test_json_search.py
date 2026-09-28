# Fill the Python code in this file
import unittest
from recursive_json_search import *
from test_data import *

class json_search_test(unittest.TestCase):
    '''test module to test search function in `recursive_json_search.py`'''

    # --- Functional tests ---
    def test_search_found(self):
        '''key should be found, return list should not be empty'''
        self.assertTrue([] != json_search(key1, data))

    def test_search_not_found(self):
        '''key should not be found, should return an empty list'''
        self.assertTrue([] == json_search(key2, data))

    def test_is_a_list(self):
        '''Should return a list'''
        self.assertIsInstance(json_search(key1, data), list)

    # --- Security tests ---
    def test_viewer_cannot_read_apiKey(self):
        '''[SR2/T1] viewer khong duoc doc apiKey'''
        self.assertEqual([], json_search("apiKey", data, role="viewer"))

    def test_viewer_cannot_read_managementIpAddress(self):
        '''[SR3/T2] viewer khong duoc doc managementIpAddress'''
        self.assertEqual([], json_search("managementIpAddress", data, role="viewer"))

    def test_unknown_role_is_denied(self):
        '''[SR5/T3] role khong hop le bi tu choi'''
        self.assertEqual([], json_search("issueSummary", data, role="hacker"))

    def test_admin_can_read_apiKey(self):
        '''[SR2] admin duoc doc apiKey'''
        result = json_search("apiKey", data, role="admin")
        self.assertTrue(len(result) > 0)

    def test_operator_can_read_managementIpAddress(self):
        '''[SR3] operator duoc doc managementIpAddress'''
        result = json_search("managementIpAddress", data, role="operator")
        self.assertTrue(len(result) > 0)

    def test_no_role_defaults_to_viewer(self):
        '''[SR6] khong truyen role -> mac dinh viewer -> apiKey bi chan'''
        self.assertEqual([], json_search("apiKey", data))

if __name__ == '__main__':
    unittest.main()

