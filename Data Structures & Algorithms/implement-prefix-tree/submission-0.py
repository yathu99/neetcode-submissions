class Node:
    def __init__(self):
        self.nextChr=dict()
class PrefixTree:

    def __init__(self):
        self.words=set()
        self.head=Node()


    def insert(self, word: str) -> None:
        self.words.add(word)
        newNode=self.head
        for letter in word:
            if(letter in newNode.nextChr.keys()):
                newNode=newNode.nextChr[letter]
            else:
                newNode.nextChr[letter]=Node()
                newNode=newNode.nextChr[letter]

    def search(self, word: str) -> bool:
        return word in self.words
                
    def startsWith(self, prefix: str) -> bool:
        newNode=self.head
        for letter in prefix:
            if(letter in newNode.nextChr.keys()):
                newNode=newNode.nextChr[letter]
            else:
                return False
        return True
        