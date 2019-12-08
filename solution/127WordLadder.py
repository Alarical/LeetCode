from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        search_dict = defaultdict(list)
        n = len(beginWord)
        # 生成dict: *ot:[hot] , h*t:[hot] , ho*:[hot]
        for word in wordList:
            for i in range(n):
                search_dict[word[:i] + '*' + word[i+1:]].append(word)

        queue = [(beginWord , 1)]
        visited = {beginWord:True}
        while queue:
            curword , level = queue.pop(0)  # hit ,1
            for i in range(n):
                tempword = curword[:i] + '*' + curword[i+1:] # *it
                for word in search_dict[tempword]:
                    #跳过 *it, 到 h*t, word = hot
                    if word == endWord:
                        return level+1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word , int(level)+1))
                #search_dict[tempword] = []
        return 0

