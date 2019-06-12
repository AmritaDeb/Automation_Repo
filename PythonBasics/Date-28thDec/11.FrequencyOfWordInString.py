#   wap to count the frequency of  words appering in a string using dictonary
class FrequencyOfWordInString:
    def freequencyOfWord(self,s):
        l = []
        l = s.split()
        print(l)
        c=0
        for i in l:
            c=l.count(i)
            print(c)
        wordfreq = [l.count(p) for p in l]
        print(dict(zip(l, wordfreq)))

ob=FrequencyOfWordInString()
s=input("Enter the string: ")
ob.freequencyOfWord(s)
