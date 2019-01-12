def leftrotate(arr,d,n):
  for i in range(d):
    operation(arr,n)

def operation(arr,n):
  temp=arr[0]
  for i in range(n-1):
    arr[i]=arr[i+1]
  arr[n-1]=temp

def printarray(arr,n):
  for i in range(n):
    print("%d"%a[i],end=' ')


size=int(input())
a=[int(x) for x in input().split()]
if(size==len(a)):
  times=int(input())
  leftrotate(a,times,size)
  printarray(a,size)
