class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        res = 0
        seen = set()
        fact = [1]
        for i in range(1, n + 1):
            fact.append(fact[-1] * i)
        
        for left in range(10 ** ((n - 1) // 2), 10 ** ((n + 1) //2)):
            l = str(left)
            r = l[::-1]
            if n % 2 == 1:
                r = r[1:]

            m = l + r
            if int(m) % k != 0:
                continue

            s = ''.join(sorted(list(m)))
            if s in seen:
                continue

            seen.add(s)
            cnt = Counter(m)
            total = fact[n]
            for key in cnt.keys():
                total //= fact[cnt[key]]

            res += total
            if 1 <= cnt['0']:
                total_non_zero = fact[n - 1]
                cnt['0'] -= 1
                for key in cnt.keys():
                    total_non_zero //= fact[cnt[key]]
                res -= total_non_zero

        return res