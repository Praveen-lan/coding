def anagram(x,y):
    return sorted(x) == sorted(y)
if(__name__=="__main__"):
    print(anagram("listen","silent"))