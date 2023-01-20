class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_letters = ['b', 'a', 'l', 'o', 'n']
        letter_frequency = dict() # Keep track of how many letters unique letters are in "balloon"

        for t in text:
            if t in balloon_letters:
                if not letter_frequency.get(t):
                    letter_frequency[t] = 1
                else:
                    letter_frequency[t] += 1
        
        res = -1
        keep_searching = True
        while keep_searching:
            res += 1
            for c in 'balloon':
                if c in letter_frequency and letter_frequency[c] > 0:
                    letter_frequency[c] -= 1
                else:
                    keep_searching = False
                    break
        
        
        return res