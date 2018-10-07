import os
import mock
import sys
import unittest

import git

if (sys.version_info > (3, 0)):
    from io import StringIO
    from importlib import reload
else:
    from StringIO import StringIO


class GitTestCase(unittest.TestCase):
    @mock.patch('git.tarfile.open')
    @mock.patch('git.os')
    @mock.patch('distutils.spawn.find_executable')
    def test_git_installation_on_import(self, find_executable_mock, os_mock,
                                        open_tarfile_mock):
        tar = mock.MagicMock()
        current_path = os.environ['PATH']

        find_executable_mock.return_value = None
        os_mock.path.return_value.isfile.return_value = False
        open_tarfile_mock.return_value = tar

        reload(git)

        open_tarfile_mock.assert_called_with(git.GIT_TAR_FILE)
        tar.extractall.assert_called_with(path=git.TMP_PATH)
        tar.close.assert_called_with()

        path = '{}:{}'.format(current_path, git.BIN_PATH)
        self.assertEqual(os.environ['PATH'], path)
        self.assertEqual(os.environ['GIT_TEMPLATE_DIR'], git.GIT_TEMPLATE_DIR)
        self.assertEqual(os.environ['GIT_EXEC_PATH'], git.GIT_EXEC_PATH)
        self.assertEqual(os.environ['LD_LIBRARY_PATH'], git.LD_LIBRARY_PATH)

    @mock.patch('git.subprocess.PIPE')
    @mock.patch('git.subprocess.Popen')
    def test_exec_command(self, PopenMock, PipeMock):
        branch_name = 'js/my_new_branch'

        PopenMock.return_value.communicate.return_value = ('output', 'error')
        PopenMock.return_value.returncode = 0
        PipeMock.return_value = StringIO()

        git.exec_command('checkout', '-b', branch_name)

        PopenMock.assert_called_with(['git', 'checkout', '-b', branch_name],
                                     stdout=PipeMock, stderr=PipeMock,
                                     cwd='/tmp', env=os.environ)
