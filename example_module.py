#!/usr/bin/python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This is an example Python module for the Python to Read the Docs
documentation repository.
It is used to show how Sphinx autodoc can be used to auto-generate
Python documentation from doc strings like this...
Written by Matthew John Hayes
"""

CONSTANT = 'example constant value'


class ExampleModule(object):
    """
    This is the main class of example_module. It doesn't do anything useful
    other than show how classes are documented by autodoc
    """

    def __init__(self):
        """
        Initialise the ExampleModule class
        """
        self.class_variable = "RANDOM"

    def run(self):
        """
        Run the ExampleModule instance
        """
        print("ExampleModule is running!")
        print("Constant is", CONSTANT)
        print("Class Variable is" + self.class_variable)
        self.increment(5)
        print("Class Variable is" + self.class_variable)

    def increment(self, value):
        """
        Increment the value of self.class_variable by value passed
        to this method
        """
        self.class_variable += value

    def _private_method(self):
        """
        Example private method that won't be documented by autodoc
        unless you add :private-members: to the automodule directive
        """
        self.class_variable += 1


if __name__ == '__main__':
    # *** Instantiate the ExampleModule class:
    example_module = ExampleModule()
    # *** Start ExampleModule:
    example_module.run()
