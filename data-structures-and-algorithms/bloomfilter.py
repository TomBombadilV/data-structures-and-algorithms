# Implementation of a Bloom Filter using Murmur3 hash

from math import ceil, log
import mmh3

class BloomFilter:

    def _num_bits(self, n: int, fpr: float) -> int:
        """
        Calculates optimal number of bits to avoid collisions based on number of 
        items being inserted (n) and given failure point rate (fpr)
        """
        return ceil(-n * log(fpr) / (log(2) ** 2))
    
    def _num_hashes(self, n: int, m: int) -> int:
        """
        Calculates optimal number of hash functions to avoid collisions based on 
        number of items being inserted (n) and number of bits (m)
        """
        return round(m / n * log(2))

    def __init__(self, n: int=1000, fpr: float=0.001):
        self.m = self._num_bits(n, fpr)  # Size of bit array
        self.k = self._num_hashes(n, self.m)  # Number of hash functions
        self.bits = 0  # Bit array stored as int 

    def add(self, key: str) -> None:
        """
        Adds key to bloom filter by creating k hashes and flipping k 
        corresponding bits
        """ 
        # Split 128 bit hash into two 64 bit halves
        h1, h2 = mmh3.hash64(key, signed=False)
        h = h1
        
        # Create k hashes using two halves and set corresponding bits to 1 
        for i in range (self.k):
            h += (h2 * self.k)
            bit = h % self.m
            self.bits |= 1 << bit

    def has(self, key: str) -> bool:
        """
        Checks if key exists in bloom filter by creating k hashes and checking 
        if all k bits are set
        """
        # Split 128 bit hash into two 64 bit halves
        h1, h2 = mmh3.hash64(key, signed=False)
        h = h1

        # Generate k hashes using two halves and check if each bit is set
        for i in range(self.k):
            h += (h2 * self.k)
            bit = h % self.m
            if not(self.bits & 1 << bit):
                return False
        return True

    def size(self) -> int:
        """
        Approximates number of items in bloom filter based on number of bits, 
        number of hash functions, and number of bits in bit array set to 1
        """
        X = bin(self.bits).count('1')  # Number of bits set to 1
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
    
    # Add fruits
    for s in added:
        bf.add(s)

    # Check size
    print(bf.size())
    
    # Check added fruits
    for s in added:
        if not(bf.has(s)):
            print("Uh oh, false negative!! Bloom filter thinks {0} exists!!".\
                  format(s))

    # Check for false positives
    for s in not_added:
        if bf.has(s):
            print('False positive: {0}'.format(s))
