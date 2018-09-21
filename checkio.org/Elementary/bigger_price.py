from operator import itemgetter

def bigger_price(limit, data):
    """
        TOP most expensive goods
    """
    # your code here
    #--------------------------------------------------------------------------
    # data0 = []
    # data1 = []
    # for i in range(len(data)):
    #     if data[i - 1]["price"] <= data[i]["price"]:
    #         data0.append(data[i])
    #     else:
    #         data0.append(data[i - 1])
    # for i in range(limit):
    #     data1.append(data0[i])
    # data1.reverse()
    # return data1
    #--------------------------------------------------------------------------
    return sorted(data, key=itemgetter("price"), reverse=True)[:limit]

if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

# These "asserts" using for self-checking and not for auto-testing
assert bigger_price(2, [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}
]) == [
    {"name": "wine", "price": 138},
    {"name": "bread", "price": 100}
], "First"

assert bigger_price(1, [
    {"name": "pen", "price": 5},
    {"name": "whiteboard", "price": 170}
]) == [{"name": "whiteboard", "price": 170}], "Second"

print('Done! Looks like it is fine. Go and check it')
