def recursion(s, l, r):
    if l >= r:
        #print("l",l+1,end=" ")
        return 1,l+1
    elif s[l] != s[r]:
        #print("l",l+1,end=" ")
        return 0,l+1
    else:
        return recursion(s, l+1, r-1)

def isPalindrome(s):

    return recursion(s, 0, len(s)-1)

#print('ABBA:', isPalindrome('ABBA'))
#print('ABC:', isPalindrome('ABC'))

n=int(input())

for _ in range(n):
    text=input()

    cnt,cnt1=isPalindrome(text)
    print(cnt,cnt1)