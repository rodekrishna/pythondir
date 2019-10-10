#Find runner up

#Sample input
#5
#2 3 6 6 5

#Sample output
#5

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    l1 = list(arr)   #Convert map into list
    l1.sort(reverse = True) #sort list in reverse order
    l2 = list(dict.fromkeys(l1)) #remove duplicates
    print(l2[1]) #print second highest (runner up)
