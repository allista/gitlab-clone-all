from typing import Iterator, Set, Dict, Union

from git import Commit, Head, Blob, Tree, TagObject

CommitSet = Set[Union[TagObject, Tree, Commit, Blob]]
HeadToCommitMap = Dict[Head, CommitSet]


class TipHandler(object):
    @staticmethod
    def _commits_per_head(heads: Iterator[Head]) -> HeadToCommitMap:
        return {head: {head.commit} | set(head.commit.iter_parents())
                for head in heads}

    @staticmethod
    def _is_tip(head: Head, commits: HeadToCommitMap) -> bool:
        tip = True
        for other in commits:
            if head.commit != other.commit:
                tip = head.commit not in commits[other]
                if not tip:
                    break
        return tip
