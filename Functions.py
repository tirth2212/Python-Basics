import operator
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
    return sorted_d
string = input("Please enter a string ")
print(most_frequent(string))
