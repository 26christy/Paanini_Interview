"""
.. :module:: test_paanini_assignment
   :synopsis: Unit test for paanini_assignment.py.
.. moduleauthor:: Christy M Thomas <26christy@gmail.com> (July 18, 2020)
"""
import unittest
import mock, sys
from io import StringIO

from Jiffy.scripts.paanini_assignment import GitInteraction 

class AssignmentTestCase(unittest.TestCase):
    @mock.patch('Jiffy.scripts.paanini_assignment.repo') 
    def test_git_commit(self, mock_repo):
        '''
        testing git_commit(). Since there is no return value
        the output of the print statement is used for the assertion
        prupose. mocked the repo to avoid making any actual changes
        in the github repository
        '''
        mock_obj = GitInteraction()
        mock_file_list = [
            '/tmp/test.txt'
        ]
        mock_file_name = [
            'test.txt'
        ]
        mock_commit_message = "mock_commit"

        read_data = '/tmp/test.txt'

        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        
        mock_open = mock.mock_open(read_data=read_data)
        with mock.patch('Jiffy.scripts.paanini_assignment.open', mock_open):
            mock_obj.git_commit(mock_file_list, mock_file_name, mock_commit_message)
            sys.stdout = sys.__stdout__
            outout = capturedOutput.getvalue().strip()

            self.assertEqual("commited to the repo", outout)

    @mock.patch('Jiffy.scripts.paanini_assignment.GitInteraction.git_commit')
    def test_initial_file(self, mock_commit):
        '''
        testing initial_file(). Since there is no return value
        the output of the print statement is used for the assertion
        prupose.
        '''
        mock_obj = GitInteraction()

        capturedOutput = StringIO()
        sys.stdout = capturedOutput

        mock_obj.initial_file()

        sys.stdout = sys.__stdout__
        outout = capturedOutput.getvalue().strip()

        self.assertEqual("Added initial.txt", outout)

    @mock.patch('Jiffy.scripts.paanini_assignment.repo')    
    @mock.patch('Jiffy.scripts.paanini_assignment.GitInteraction.git_commit')
    def test_processed_file(self, mock_commit, mock_repo):
        '''
        testing processed_file(). Since there is no return value
        the output of the print statement is used for the assertion
        prupose.
        '''
        mock_obj = GitInteraction()

        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        mock_obj.processed_file()

        sys.stdout = sys.__stdout__
        outout = capturedOutput.getvalue().strip()

        self.assertEqual("Added processed.txt", outout)

if __name__ == '__main__':
    unittest.main()
