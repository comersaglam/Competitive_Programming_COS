from collections import deque
class Trie:
    def __init__(self):
        self.trie = dict()

    def add_word(self,word):
        if self.search_word(word):
            return False
        node = self.trie
        for char in word:
            if char not in node:
                node[char]=dict()
            node=node[char]
        node['end']=True
        return True

    def search_word(self,word):
        node = self.trie
        for char in word:
            if not char in node:
                return False
            node = node[char]
        return 'end' in node

    def search_prefix(self,prefix):
        node = self.trie
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

    def search_bar(self,prefix):
        node = self.trie
        for char in prefix:
            if char not in node:
                return []
            node = node[char]

        result = []
        queue = deque([(prefix,node)])
        while queue:
            cur_prefix,cur_node = queue.popleft()
            for char in cur_node:
                if char == 'end':
                    result.append(cur_prefix)
                else:
                    queue.append((cur_prefix+char,cur_node[char]))


        return result

trie = Trie()
trie.add_word('apple')
trie.add_word('app')
trie.add_word('banana')
trie.add_word('ban')
trie.add_word('band')
print(trie.search_word('apple'))
print(trie.search_word('app'))
print(trie.search_word('banana'))
print(trie.search_prefix('ban'))
print(trie.search_bar('ban'))