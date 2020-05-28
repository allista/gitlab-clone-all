import os
import traceback

import sys
from git import Repo, InvalidGitRepositoryError


class RepoProcessor(object):
    def __init__(self, args, path='.'):
        self._args = args
        self._path = path

    def _process_path(self, path: str) -> None:
        try:
            os.chdir(path)
            try:
                repo = Repo(path)
            except InvalidGitRepositoryError:
                return
            if repo.bare:
                return
            self._process(repo, path)
        except Exception as ex:
            print('Error while processing {}:\n{!s}\n{}'
                  .format(path, ex, traceback.format_exc()))

    def run(self) -> int:
        start_path = os.path.abspath(self._path)
        self._process_path(start_path)
        for root, dirs, _files in os.walk(start_path):
            for dirname in dirs:
                if dirname == '.git':
                    continue
                self._process_path(os.path.join(root, dirname))
        return 0

    def _process(self, repo, path):
        raise NotImplementedError()

    @classmethod
    def execute(cls, parser, path='.'):
        args = parser.parse_args()
        sys.exit(cls(args, path).run())
