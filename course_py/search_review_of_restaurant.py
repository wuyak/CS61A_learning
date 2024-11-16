import json

def search(query, ranking=lambda r: -r.stars):
    rest_results = [r for r in Restaurant.all if query in r.name]
    return sorted(rest_results, key=ranking)

def reviewed_both(r, s):
    return fast_overlap(r.reviewers, s.reviewers)

def fast_overlap(s, t):
    """
    >>> fast_overlap([3,4,6,7,9,10], [1,3,5,7,8])
    2
    """
    i, j, count = 0, 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            count, i, j = count+1, i+1, j+1
        elif s[i] < t[j]:
            i += 1
        else:
            j += 1
    return count



class Restaurant:
    all = []
    def __init__(self, name, stars, reviewers):
        self.name, self.stars = name, stars
        self.reviewers = reviewers
        Restaurant.all.append(self)

    def similar(self, k, similarity=reviewed_both):
        others = list(Restaurant.all)
        others.remove(self)
        return sorted(others, key= lambda r: -similarity(self,r))[:k]
    def __repr__(self):
        return '<' + self.name + '>'


reviewers_for_restaurant = {}
with open('reviewers.json', 'r', encoding='utf-8') as file:
    for line in file:
        r = json.loads(line)
        biz = r['business_id']
        if biz not in reviewers_for_restaurant:
            reviewers_for_restaurant[biz] = [r['user_id']]
        else:
            reviewers_for_restaurant[biz].append(r['user_id'])

with open('restaurants.json', 'r', encoding='utf-8') as file:
    for line in file:
        r = json.loads(line)
        reviewers = reviewers_for_restaurant[r['business_id']]
        Restaurant(r['name'], r['stars'], sorted(reviewers))

while True:
    print('>', end='')
    results = search(input().strip())
    for r in results:
        print(r, 'is similiar to', r.similiar(3))
