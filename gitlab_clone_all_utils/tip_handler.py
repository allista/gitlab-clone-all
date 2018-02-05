class TipHandler(object):
    @staticmethod
    def _commits_per_head(heads):
        return {head: set([head.commit] + list(head.commit.iter_parents()))
                for head in heads}

    @staticmethod
    def _is_tip(head, commits):
        tip = True
        for other in commits:
            if head != other:
                if head.commit in commits[other]:
                    tip = False
                    break
        return tip
