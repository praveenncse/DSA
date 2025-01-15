class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        res = 0
        cur_vowel_count = 0

        for i in range(len(s)):
            if s[i] in vowels:
                cur_vowel_count += 1

            if i >= k and s[i - k] in vowels:
                cur_vowel_count -= 1

            if i >= k - 1:
                res = max(res, cur_vowel_count)

        return res
