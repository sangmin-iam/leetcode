# ["John","johnsmith@mail.com","john_newyork@mail.com"] - 이메일 같음
# ["John","johnsmith@mail.com","john00@mail.com"] - 이메일 같음
# ["Mary","mary@mail.com"]
# ["John","johnnybravo@mail.com"]]

# 주의
# 같은 이름이 존재한다고 해서 동일 인물이 아님
# 같은 이메일이 1개라도 존재한다면 같은 사람

class UnionFind:
    def __init__(self, n):
        self.leader = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, x):
        cur = x
        while cur != self.leader[cur]:
            self.leader[cur] = self.leader[self.leader[cur]]
            cur = self.leader[cur]
        return cur
    
    def union(self, a, b):
        leader_a = self.find(a)
        leader_b = self.find(b)

        if leader_a == leader_b:
            return False
        
        if self.size[leader_a] > self.size[leader_b]:
            self.leader[leader_b] = leader_a
            self.size[leader_a] += 1
        else:
            self.leader[leader_a] = leader_b
            self.size[leader_b] += 1
        return True
        

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAcc = {} # email -> index of acc

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    uf.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i
        
        emailGroup = defaultdict(list) # index of acc -> list of emails
        
        for email, i in emailToAcc.items(): # Key, Value Pair 
            leader = uf.find(i)
            emailGroup[leader].append(email)

        res = []
        for i, email in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i])) # arr concat
        
        return res