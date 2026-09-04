from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        indeg = {c: 0 for c in adj}

        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        indeg[c2] += 1
                    break
            else:
                if len(w1) > len(w2):
                    return ""          # w2 is a proper prefix of w1

        q = deque(c for c in indeg if indeg[c] == 0)
        out = []
        while q:
            c = q.popleft()
            out.append(c)
            for nxt in adj[c]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)

        return "".join(out) if len(out) == len(indeg) else ""