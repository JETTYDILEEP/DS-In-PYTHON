def binarySearch(arr,start,end): 
  
  while start<=end:      
    mid=int((start+end)/2) 
    if(arr[mid]>arr[mid+1]): 
      if (arr[start]<=arr[mid]): 
        start = mid + 1
      elif(arr[start]>=arr[mid]):
        end = mid - 1
    else:
      print('pivot element is',mid+1)  
    
  
  
  
s=int(input('enter size of array :'))

print('enter elements of array in below:')
arr = [int(x) for x in input().split()] 
start=0
end=s
t=arr
t.sort()
if(s==len(arr) and t==arr):
  binarySearch(arr,start,end) 
