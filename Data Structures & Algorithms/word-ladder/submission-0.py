from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        minimum_solution_so_far = 101
        queue = deque([(beginWord, 1)])
        visited = set()
        while queue:
            word, counter = queue.popleft()
            if word == endWord:
                minimum_solution_so_far = min(minimum_solution_so_far, counter)
            else:
                for word in self.differnt_by_one(word):
                    if word in wordList and word not in visited:
                        queue.append([word, counter+1])
                        visited.add(word)
        if minimum_solution_so_far == 101:
            return 0
        else:
            return minimum_solution_so_far
    def differnt_by_one(self, word):
        wordlist = []
        alphabet = "abcdefghijklmnopqrstuvxyz"
        for i in range(len(word)):
            for letter in alphabet:
                if word[i] != letter:
                    wordlist.append(word[:i] + letter + word[i+1:])
        return wordlist

        
