import collections
from typing import List

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
      queue = collections.deque([(id, 0)])
      seen = set()
      ans = {}

      while queue:
          id, depth = queue.popleft()
          seen.add(id)
          if depth == level:
              if id in ans:
                  ans[id] += 1
              else:
                  ans[id] = 1

          for friend in friends[id]:
              if friend not in seen:
                  queue.append((friend, depth+1))

      return sorted(ans, key = lambda x: (ans[id], id))
