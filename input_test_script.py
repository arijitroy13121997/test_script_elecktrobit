import json
import unittest


class InputTestScript(unittest.TestCase):

    def initialize(self, file):
        self.file = file

    def runTest(self):
        self.test_process_name()

    def _is_valid_json(self):
        '''Check if value is numeric'''
        try:
            return json.load(self.file)
        except ValueError:
            return None

    def test_process_name(self):
        '''check is process name APP1'''

        data = self._is_valid_json()
        self.assertIsNotNone(data, "Json is not valid")
        self.assertTrue("process" in data, "Process not found")
        self.assertTrue("env" in data.get('process'), "process.env not found")

        env_variables = data.get('process').get('env')
        process_var = list(
            filter(lambda str: str.startswith("PROCESS_NAME="), env_variables))
        self.assertNotEqual(len(process_var), 0, "Process Name not available")
        self.assertEqual(len(process_var), 1,
                         "Duplicate Process name entry found")
        key_val_pair = process_var[0].split("=", 1)

        self.assertEqual(key_val_pair[1].strip(),
                         "APP1", "Process Name is invalid")


if __name__ == '__main__':
    unittest.main()
