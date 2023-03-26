numbers = [45, 98, "ab","cd", 56, 75]
numbers2 = [1,1,2,-2,5,2,4,4,-1,-2,5]
count = 0

# print all item that are less than or equal to 50
for i in range(0,len(numbers)):
    if type(numbers[i])==int:
        print(numbers[i])
        continue

def odd(n):
 count = 0
 for i in range(0,len(numbers2)):
    if numbers2[i] == n:
        count = count + 1
        continue
 return count

ans= 0
ans = odd(-1)
if(ans == 1 or ans == 3 or ans ==5):
    print("Number is at",ans ,"odd time")

