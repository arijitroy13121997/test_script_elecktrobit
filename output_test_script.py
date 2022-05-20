
import unittest
import re


class OutputTestScript(unittest.TestCase):

    def initialize(self, file):
        self.file = file

    def runTest(self):
        self.test_process_name()

    def test_process_name(self):
        for line in self.file:
            line = line.strip()

            if self._is_send_data_log(line):
                self._test_send_data_log(line)
            elif self._is_data_read_log(line):
                self._test_data_read_log(line)

    def _set_values_in_dict(self, match):
        '''keep values as key-valie pair'''
        value_map = {}
        key = None
        value = None
        count = 0

        for item in match[0]:
            if (count % 2 == 0):
                key = item
            else:
                value = int(item)
                value_map[key] = value
            count += 1
        return value_map

    def _is_send_data_log(self, line):
        ''' Check if send data pattern available'''
        return re.search("\[Send  data: (?:\s*(\w+?)=\s*(-?[0-9]*))*]", line)

    def _is_data_read_log(self, line):
        # Check if send data pattern available
        return re.search("\[Data Read: (?:\s*(\w+?):\s*(-?[0-9]*))*]", line)

    def _test_send_data_log(self, line):
        ''' Check if send data pattern available'''
        matches = re.findall(
            "\[Send  data: (?:\s*(\w+?)=\s*(-?[0-9]*))(?:\s*(\w+?)=\s*(-?[0-9]*))]", line)
        value_map = self._set_values_in_dict(matches)

        self.assertTrue("value_1" in value_map, "value_1 is not available")
        self.assertTrue("value_2" in value_map, "value_1 is not available")
        self.assertTrue(50 <= value_map.get("value_1") <=
                        200, "Value_1 is out of range.")
        self.assertTrue(0 <= value_map.get("value_2") <=
                        150, "Value_2 is out of range")

    def _test_data_read_log(self, line):
        matches = re.findall(
            "\[Data Read: (?:\s*(\w+?):\s*(-?[0-9]*))*]", line)
        value_map = self._set_values_in_dict(matches)
        self.assertTrue("Checksum" in value_map, "Checksum is out of range")
        self.assertTrue(0 <= value_map.get("Checksum") <= 2)
