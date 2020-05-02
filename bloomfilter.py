# Implementation of a Bloom Filter using Murmur3

from math import ceil, log
import mmh3

class BloomFilter:

    def _num_bits(self, n: int, fpr: float) -> int:
        return ceil(-n * log(fpr) / (log(2) ** 2))
    
    def _num_hashes(self, n: int, m: int) -> int:
        return round(m / n * log(2))

    def __init__(self, n: int=1000, fpr: float=0.001):
        self.m = self._num_bits(n, fpr)
        self.k = self._num_hashes(n, self.m)
        print(self.m, self.k)
        self.bits = 0

    def add(self, key: str) -> None:
        h1, h2 = mmh3.hash64(key, signed=False)
        h = h1
        for i in range (self.k):
            h += (h2 * self.k)
            bit = h % self.m
            self.bits |= 1 << bit

    def has(self, key: str) -> bool:
        h1, h2 = mmh3.hash64(key, signed=False)
        h = h1
        for i in range(self.k):
            h += (h2 * self.k)
            bit = h % self.m
            if not(self.bits & 1 << bit):
                return False
        return True

    def size(self) -> int:
        X = bin(self.bits).count('1')
        return round(-(self.m / self.k) * log(1 - (X / self.m)))

if __name__ == '__main__':
    bf = BloomFilter(20)
    
    added = [ 'apple', 'grape', 'pear', 'banana', 'plum', 'peach', 'orange', 
              'jackfruit', 'apricot', 'cherry', 'blackberry', 'watermelon',
              'cantaloupe', 'lemon', 'blueberry', 'durian', 'tomato?', 'kiwi',
              'pineapple', 'dragonfruit', 'longan', 'lime', 'lychee', 
              'papaya', 'persimmon', 'pomegranate', 'mandarin', 'starfruit']
    
    not_added = ['squash', 'cucumber', 'beet', 'carrot', 'potato', 'corn', 
                 'spinach', 'bok choy', 'string bean', 'arugula', 'asparagus',
                 'cabbage', 'lettuce', 'zucchini', 'kale', 'u wot m8']
    for s in added:
        bf.add(s)

    print(bf.size())
    
    for s in added:
        if not(bf.has(s)):
            print("Uh oh, false negative!! Something is wrong")
        else:
            print("Bloom filter might have {0}".format(s))
    
    for s in not_added:
        if bf.has(s):
            print('False positive: {0}'.format(s))
