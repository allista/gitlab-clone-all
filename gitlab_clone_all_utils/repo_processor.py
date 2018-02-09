import os
import traceback

import sys
from git import Repo, InvalidGitRepositoryError


class RepoProcessor(object):
    def __init__(self, args, path='.'):
        self._args = args
        self._path = path

    def run(self):
        os.chdir(self._path)
        root = os.getcwd()
        for entry in sorted(os.listdir('.')):
            path = os.path.join(root, entry)
            if os.path.isdir(path):
                os.chdir(path)
                try:
                    try:
                        repo = Repo(path)
                    except InvalidGitRepositoryError:
                        continue
                    if repo.bare:
                        continue
                    self._process(repo, path)
                except Exception as ex:
                    print('Error while processing {}:\n{!s}\n{}'
                          .format(path, ex, traceback.format_exc()))
        return 0

    def _process(self, repo, path):
        raise NotImplementedError()

    @classmethod
    def execute(cls, parser, path='.'):
        args = parser.parse_args()
        sys.exit(cls(args, path).run())
