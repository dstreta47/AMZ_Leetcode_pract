from collections import defaultdict, Counter
from itertools import combinations
def analyser(username,timestamp,website):
    users = defaultdict(list)
    for user,time,site in sorted(zip(username,timestamp,website),key=lambda x: (x[0],x[1])):
        users[user].append(site)

    pattern = Counter()
    for user, sites in users.items():
        pattern.update(Counter(set(combinations(sites,3))))

    print(max(sorted(pattern,key=pattern.get)))  


username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]
print(analyser(username,timestamp,website))
