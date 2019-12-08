from collections import defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return []
        search_dict = defaultdict(list)
        n = len(beginWord)
        # 生成dict: *ot:[hot] , h*t:[hot] , ho*:[hot]
        for word in wordList:
            for i in range(n):
                search_dict[word[:i] + '*' + word[i+1:]].append(word)

        queue = [(beginWord ,[beginWord] ,  1)]
        visited = {beginWord:1}
        ans = []
        firstfound = True
        min_len = 0
        #print ('ok')
        while queue:
            curword ,curpath , level = queue.pop(0)  # hit ,1
            for i in range(n):
                tempword = curword[:i] + '*' + curword[i+1:] # *it
                for word in search_dict[tempword]:
                    #跳过 *it, 到 h*t, word = hot
                    if word == endWord:
                        if firstfound:
                            min_len = level+1
                            firstfound = False
                            ans.append(curpath + [word])
                        else:
                            if level + 1> min_len:
                                return ans
                            else:
                                ans.append(curpath + [word])
                    if word in visited and visited[word] < level + 1:
                        continue
                    else:
                        visited[word] = level+1
                        queue.append((word , curpath + [word] , level+1))
                #search_dict[tempword] = []
        return ans