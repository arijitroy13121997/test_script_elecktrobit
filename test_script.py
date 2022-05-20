import unittest
import argparse
from input_test_script import InputTestScript
from output_test_script import OutputTestScript


def main():

    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        "--inputfile", "-i", type=str,   required=True)
    argument_parser.add_argument("--outputfile", "-o", type=str, required=True)
    arguments = argument_parser.parse_args()

    input_file_argument = (arguments.inputfile)
    output_file_argument = (arguments.outputfile)

    input_file = open(input_file_argument, "r")
    output_file = open(output_file_argument, "r")

    input_test_script_config = InputTestScript()
    input_test_script_config.initialize(input_file)

    output_test_script_config = OutputTestScript()
    output_test_script_config.initialize(output_file)

    suite = unittest.TestSuite()
    suite.addTest(input_test_script_config)
    suite.addTest(output_test_script_config)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    main()
