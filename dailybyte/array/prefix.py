def getPrefix(s):
    prefix = ""
    for idx,char in enumerate(s[0]):
        if charGood(idx,char,s):
            prefix += char
        else:
            break
    return prefix

def charGood(index,char,words):
    for word in words:
        if word[index] != char:
            return False
    return True

arr1 = ["colorado", "color", "cold"]
arr2 = ["a","b","c"]
arr3 = ["spot", "spotty", "spotted"]
print(getPrefix(arr3))

# ["colorado", "color", "cold"], return "col"
# ["a", "b", "c"], return ""
# ["spot", "spotty", "spotted"], return "spot