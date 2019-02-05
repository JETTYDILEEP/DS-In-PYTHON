def binarySearch(arr,start,end,x): 
  while start<=end:      
    mid=int((start+end)/2) 
    if (arr[mid]==x): 
      print('required element is',x,'at',mid+1)
      break 
    elif (arr[mid] < x): 
      start = mid + 1
    else: 
      end = mid - 1
      
    
  return -1
  
  
s=int(input('enter size of array :'))
e=int(input('enter element to be searched :'))
print('enter elements of array in below:')
arr = [int(x) for x in input().split()] 
t=arr
t.sort()
if(s==len(arr) and t==arr):
  binarySearch(arr,0,s-1,e) 
  
